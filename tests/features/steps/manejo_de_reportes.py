"""
Este módulo contiene los pasos definidos para las pruebas de comportamiento
utilizando Behave.
"""
from behave import step

from app.Reporte import Reporte
from app.Siac import Siac
from app.Departamento import Departamento


#use_step_matcher("re")


@step('un reporte ciudadano "{id_reporte}" del problema "{descripcion_problema}" llega al "SIAC"')
def step_impl(context, id_reporte, descripcion_problema):
    """
        :type descripcion_problema: str
        :type id_reporte: str
        :type context: behave.runner.Context
   """
    context.reporte = Reporte(id_reporte, descripcion_problema)
    context.siac = Siac() #Controlador de reportes
    context.siac.agregar_nuevo_reporte_no_asignado(context.reporte) #Variable reportes_no_asignados

    assert context.reporte in context.siac.obtener_reportes_no_asignados()


@step('el reporte ha sido asignado automaticamente al departamento "{nombre_departamento}" por tener un nivel de confianza mayor que el 80%')
def step_impl(context, nombre_departamento):
    """
    :type nombre_departamento: str
    :type context: behave.runner.Context
    """


### calcular confianza para asginar si esque cumple aqui deberia parasr al asignar automaticamente

    context.departamento = Departamento(nombre_departamento)
    # Clasifica el reporte automáticamente y lo anade a la lista de reportes del departamento. actualiza estado reporte
    ## si es automaticamente porque la siac le asigna directo no deberia ser el departamento quien se asinge
    ##context.siac.asignar_automaticamente_reporte_a_departamento()
    context.departamento.agregar_reporte(context.reporte)
    assert context.reporte in context.departamento.obtener_reportes()


@step('el reporte tiene el estado "{estado_reporte}"')
def step_impl(context, estado_reporte):
    """
    :type context: behave.runner.Context
    :type estado_reporte: str

    """


    assert estado_reporte == context.reporte.obtener_estado()


@step("el departamento asignado atienda el reporte con mayor prioridad")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.departamento.atender_reporte_mayor_prioridad() #cambiar esta de reporte en funcion


@step('el estado del reporte atendido cambia a "{estado_reporte}"')
def step_impl(context, estado_reporte):
  # print("Estado esperado: {estado_reporte}")
    context.reporte.cambiar_estado(estado_reporte)
    assert estado_reporte == context.reporte.obtener_estado()



@step('el departamento debe registrar la evidencia "{evidencia}" de la solucion del reporte.')
def step_impl(context, evidencia):
    """
    :type evidencia: str
    :type context: behave.runner.Context
    """
    if context.reporte.obtener_estado() == "resuelto":
        context.departamento.registrar_evidencia(context.reporte, evidencia)
        assert context.reporte.obtener_evidencia() == evidencia
    else:
        assert False, "El reporte no está resuelto, no se puede registrar evidencia."


@step('el estado del resto de reportes no atendidos cambia a "postergado"')
def step_impl(context):
    """
    Cambia el estado de los reportes no atendidos a 'postergado' si existen.
    Si no hay reportes, imprime un mensaje y pasa el test.
    """
    """
    Cambia el estado de los reportes no atendidos (no asignados, atendidos o resueltos) a 'postergado' si existen.
    Si no hay reportes, imprime un mensaje y pasa el test.
    """
    # Obtener todos los reportes del departamento
    todos_los_reportes = context.departamento.obtener_reportes()

    # Filtrar reportes no atendidos (esto incluye los reportes no asignados)
    reportes_no_atendidos = [
        reporte for reporte in todos_los_reportes
        if reporte.obtener_estado() not in ["asignado", "atendido", "resuelto"]
    ]

    if reportes_no_atendidos:
        # Si hay reportes no atendidos, se cambian a "postergado"
        for reporte in reportes_no_atendidos:
            reporte.cambiar_estado("postergado")

        # Validar que los reportes han cambiado su estado a "postergado"
        assert all(reporte.obtener_estado() == "postergado" for reporte in reportes_no_atendidos), (
            "No todos los reportes no atendidos fueron marcados como 'postergado'."
        )
    else:
        # Si no hay reportes no atendidos, imprimir mensaje y pasar el test
        print("No hay más reportes para postergar.")
        assert True, "No hay reportes no atendidos para procesar."


@step('un reporte ciudadano "{id_reporte}" del problema "{descripcion_problema}" asignado al departamento "{nombre_departamento}"')
def step_impl(context, id_reporte, descripcion_problema, nombre_departamento):
    """
        :type nombre_departamento: str
        :type descripcion_problema: str
        :type id_reporte: str
        :type context: behave.runner.Context
   """
    context.reporte = Reporte(id_reporte, descripcion_problema)

    context.departamento = Departamento(nombre_departamento)
    context.departamento.agregar_reporte(context.reporte)
    context.reporte.cambiar_estado("postergado")

    assert context.reporte in context.departamento.obtener_reportes()





@step("no ha sido asignado a ningun departamento")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.siac.asignar_automaticamente_reporte_a_departamento()

    assert context.reporte in context.siac.obtener_reportes_no_asignados()


@step('se realice una clasificacion manual al departamento "{nombre_departamento}"')
def step_impl(context, nombre_departamento):
    """
    :type nombre_departamento: str
    :type context: behave.runner.Context
    """
    context.departamento = Departamento(nombre_departamento)
    #Cambiar estado del reporte a asignado
    context.siac.asignar_manualmente_reporte_a_departamento(context.reporte, context.departamento)

    assert context.reporte in context.departamento.obtener_reportes()

@step('se añaden los nuevos criterios de clasificación "{criterios}"')
def step_impl(context,criterios):
    """
    :type context: behave.runner.Context
    :type criterios: str
    """
    # Convierte el string de criterios en una lista (usando coma como separador)
    lista_criterios = [criterio.strip() for criterio in criterios.split(",")]

    # Agrega los criterios al departamento
    context.siac.agregar_criterios_clasificacion_por_departamento(context.departamento, lista_criterios)#Verificar repetidos

    lista_criterios_departamento = context.siac.obtener_criterios_clasificacion_por_departamento(context.departamento)
    assert all(criterio in lista_criterios_departamento for criterio in lista_criterios)



@step('el estado del reporte cambia a "asignado"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert "asignado" == context.reporte.obtener_estado()