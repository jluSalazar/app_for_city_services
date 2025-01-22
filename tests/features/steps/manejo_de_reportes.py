"""
Este módulo contiene los pasos definidos para las pruebas de comportamiento
utilizando Behave.
"""
from behave import step

from app.models import Departamento


#use_step_matcher("re")


@step('un reporte ciudadano "{id_reporte}" del problema "{descripcion_problema}"')
def step_impl(context, id_reporte, descripcion_problema):
    """
        :type id_reporte: str
        :type context: behave.runner.Context
        :type descripcion_problema: str
   """
    context.reporte = Reporte(id_reporte, descripcion_problema)

    assert context.reporte.obtener_id == id_reporte


@step("su nivel de confianza de clasificacion es mayor que el 80% para cualquier departamento")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.reporte.clasificar()
    context.departamento = context.reporte.obtener_departamento_asignado()
    assert 80 <= context.reporte.obtener_nivel_confianza


@step('el reporte tiene el estado "{estado_reporte}"')
def step_impl(context, estado_reporte):
    """
    :type context: behave.runner.Context
    :type estado_reporte: str
    """
    assert estado_reporte == context.reporte.obtener_estado()


@step("los recursos del departamento asignado sean necesarios para resolver el problema")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.departamento.tiene_recursos_disponibles()


@step('el estado del reporte cambia a "{estado_reporte}"')
def step_impl(context, estado_reporte):
    """
    :type estado_reporte: str
    :type context: behave.runner.Context
    """
    context.reporte.cambiar_estado(estado_reporte)
    assert estado_reporte == context.reporte.obtener_estado()


@step("el departamento debe registrar la evidencia de la solucion del reporte.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.departamento.registrar_evidencia(context.reporte)
    assert context.reporte.obtener_evidencia() is not None


@step("los recursos del departamento asignado no sean suficientes para resolver el problema")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert not context.departamento.tiene_recursos_disponibles()


@step("su nivel de confianza de clasificacion es menor que el 80% para cualquier departamento")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@step('se realice una clasificacion manual al departamento "nombre_departamento"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.reporte.clasificar()
    context.departamento = context.reporte.obtener_departamento_asignado()
    assert 80 > context.reporte.obtener_nivel_confianza

@step('se añaden los nuevos criterios de clasificación "{criterios}"')
def step_impl(context,criterios):
    """
    :type context: behave.runner.Context
    :type criterios: str
    """
    # Convierte el string de criterios en una lista (usando coma como separador)
    lista_criterios = [criterio.strip() for criterio in criterios.split(",")]

    # Agrega los criterios al departamento
    for criterio in lista_criterios:
        context.departamento.agregar_criterios_clasificacion(criterio)

    for criterio in lista_criterios:
        assert criterio in context.departamento.obtener_criterios_clasificacion(), \
            f"El criterio '{criterio}' no se añadió correctamente."
