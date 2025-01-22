"""
Este módulo contiene los pasos definidos para las pruebas de comportamiento
utilizando Behave.
"""
from behave import step
#use_step_matcher("re")


@step('un reporte ciudadano "{id_reporte}" del problema "{descripcion_problema}"')
def step_impl(context, id_reporte, descripcion_problema):
    """
        :param id_reporte: str
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
    raise NotImplementedError(
        u'STEP: Cuando los recursos del departamento asignado sean necesarios para resolver el problema')


@step('el estado del reporte cambia a "resuelto"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces el estado del reporte cambia a "resuelto"')


@step("el departamento debe registrar la evidencia de la solucion del reporte\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y el departamento debe registrar la evidencia de la solucion del reporte.')


@step("los recursos del departamento asignado no sean suficientes para resolver el problema")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Cuando los recursos del departamento asignado no sean suficientes para resolver el problema')


@step("el departamento")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y el departamento')


@step("su nivel de confianza de clasificacion es menor que el 80% para cualquier departamento")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Y su nivel de confianza de clasificacion es menor que el 80% para cualquier departamento')


@step('se realice una clasificacion manual al departamento "nombre_departamento"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se realice una clasificacion manual al departamento "nombre_departamento"')


@step("se añaden los nuevos criterios de clasificación")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y se añaden los nuevos criterios de clasificación')