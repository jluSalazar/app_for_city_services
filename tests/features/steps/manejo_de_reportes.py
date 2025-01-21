from datetime import datetime, timedelta
from behave import *
from app.models import EstadoReporte, Reporte, Departamento, Evidencia, SolucionReporte


class SistemaClasificacion:
    def __init__(self):
        self.palabras_clave = {
            "Obras Públicas": ["bache", "pavimento", "calle", "vereda"],
            "Alumbrado Público": ["luminaria", "luz", "poste", "alumbrado"],
            "Limpieza Pública": ["basura", "residuos", "desperdicios"],
            "Parques y Jardines": ["árbol", "planta", "parque", "jardín"]
        }

    def clasificar(self, descripcion: str) -> tuple[str, float]:
        mejor_departamento = None
        mejor_confianza = 0

        for depto, palabras in self.palabras_clave.items():
            coincidencias = sum(1 for palabra in palabras if palabra in descripcion.lower())
            confianza = (coincidencias / len(palabras)) * 100

            if confianza > mejor_confianza:
                mejor_confianza = confianza
                mejor_departamento = depto

        return mejor_departamento, mejor_confianza

    def agregar_palabras_clave(self, departamento, palabras):
        if departamento in self.palabras_clave:
            self.palabras_clave[departamento].extend(palabras)
        else:
            self.palabras_clave[departamento] = palabras

# Clasificación Automática
@step('un nuevo reporte ciudadano del problema "{descripcion_reporte}"')
def step_nuevo_reporte(context, descripcion_reporte):
    context.reporte = Reporte(
        id=1,
        descripcion=descripcion_reporte,
        estado=EstadoReporte.CLASIFICANDO,
        fecha_creacion=datetime.now(),
        ubicacion="ubicación de prueba"
    )


@step('el sistema encuentra coincidencias con el departamento "{departamento}"')
def step_encuentra_coincidencias(context, departamento):
    context.sistema_clasificacion = SistemaClasificacion()
    context.departamento_detectado, context.confianza = context.sistema_clasificacion.clasificar(
        context.reporte.descripcion)
    assert context.departamento_detectado == departamento


@step('el nivel de confianza "{confianza}"% es mayor que 80%')
def step_nivel_confianza(context, confianza):
    context.nivel_confianza = float(confianza)
    assert context.nivel_confianza > 80


@step('el reporte se clasifica como "asignado"')
def step_clasificar_asignado(context):
    context.reporte.cambiar_estado(EstadoReporte.ASIGNADO)
    assert context.reporte.estado == EstadoReporte.ASIGNADO


@step('se asigna al departamento "{departamento}"')
def step_asignar_departamento(context, departamento):
    context.reporte.departamento = Departamento(id=1, nombre=departamento)
    assert context.reporte.departamento.nombre == departamento


# Fallo en Clasificación
@step('el sistema no puede determinar el departamento responsable ya que el nivel de confianza es menor a 80%')
def step_fallo_clasificacion(context):
    context.sistema_clasificacion = SistemaClasificacion()
    _, context.confianza = context.sistema_clasificacion.clasificar(context.reporte.descripcion)
    assert context.confianza < 80


@step('el reporte se marca como "noAsignado"')
def step_marcar_no_asignado(context):
    context.reporte.cambiar_estado(EstadoReporte.NO_ASIGNADO)
    assert context.reporte.estado == EstadoReporte.NO_ASIGNADO


# Clasificación Manual
@step('un reporte "noClasificado"')
def step_reporte_no_clasificado(context):
    context.reporte = Reporte(
        id=1,
        descripcion="Reporte de prueba",
        estado=EstadoReporte.NO_ASIGNADO,
        fecha_creacion=datetime.now(),
        ubicacion="ubicación de prueba"
    )


@step('el departamento de quejas asigna el departamento "{departamento}"')
def step_asignacion_manual(context, departamento):
    context.departamento_asignado = Departamento(id=1, nombre=departamento)
    context.reporte.departamento = context.departamento_asignado


@step('registra la justificación "{justificacion}"')
def step_registrar_justificacion(context, justificacion):
    context.justificacion = justificacion


@step('el reporte cambia a "asignado"')
def step_cambiar_resolviendo(context):
    context.reporte.cambiar_estado(EstadoReporte.ASIGNADO)
    assert context.reporte.estado == EstadoReporte.ASIGNADO

@step('se añaden los nuevos criterios de clasificación "{palabras_clave}"')
def step_anadir_criterios(context, palabras_clave):
    context.sistema_clasificacion = SistemaClasificacion()
    context.sistema_clasificacion.agregar_palabras_clave(context.departamento, palabras_clave)


# Inicio de Atención
@step('un reporte "asignado" al departamento "{departamento}"')
def step_reporte_asignado(context, departamento):
    context.reporte = Reporte(
        id=1,
        descripcion="Reporte de prueba",
        estado=EstadoReporte.ASIGNADO,
        fecha_creacion=datetime.now(),
        ubicacion="ubicación de prueba",
        departamento=Departamento(id=1, nombre=departamento)
    )


@step('el departamento tiene recursos disponibles')
def step_recursos_disponibles(context):
    context.reporte.departamento.recursos_disponibles = True


@step('el reporte cambia a "resolviendo"')
def step_cambiar_resolviendo(context):
    context.reporte.cambiar_estado(EstadoReporte.RESOLVIENDO)
    assert context.reporte.estado == EstadoReporte.RESOLVIENDO


# Postergación
@step('el departamento "{departamento}" no tiene recursos disponibles')
def step_sin_recursos(context, departamento):
    context.reporte.departamento.recursos_disponibles = False


@step('el reporte cambia a "postergado"')
def step_cambiar_postergado(context):
    context.reporte.cambiar_estado(EstadoReporte.POSTERGADO)
    assert context.reporte.estado == EstadoReporte.POSTERGADO


@step('el departamento registra el motivo "{motivo}"')
def step_registrar_motivo(context, motivo):
    context.reporte.motivo_postergacion = motivo


@step('el departamento establece una fecha estimada "{fecha_estimada}" para atender el reporte')
def step_establecer_fecha(context, fecha_estimada):
    dias = int(fecha_estimada.split()[0])
    context.reporte.fecha_estimada = datetime.now() + timedelta(days=dias)


# Resolución
@step('el personal municipal registra')
def step_registrar_solucion(context):
    context.solucion = {row['acción realizada']: row['<accion>'] for row in context.table}


@step('adjunta fotos del trabajo realizado')
def step_adjuntar_fotos(context):
    context.evidencia = Evidencia(
        descripcion="Evidencia de trabajo realizado",
        fotos=["foto1.jpg", "foto2.jpg"],
        fecha_registro=datetime.now()
    )


@step('el reporte cambia a "solucionado"')
def step_cambiar_solucionado(context):
    context.reporte.cambiar_estado(EstadoReporte.SOLUCIONADO)
    assert context.reporte.estado == EstadoReporte.SOLUCIONADO


# Reapertura
@step('un reporte "solucionado"')
def step_reporte_solucionado(context):
    context.reporte = Reporte(
        id=1,
        descripcion="Reporte de prueba",
        estado=EstadoReporte.SOLUCIONADO,
        fecha_creacion=datetime.now(),
        ubicacion="ubicación de prueba"
    )


@step('el ciudadano indica que el problema persiste')
def step_problema_persiste(context):
    context.reapertura = True


@step('proporciona nueva evidencia fotográfica "{evidencia}"')
def step_nueva_evidencia(context, evidencia):
    context.nueva_evidencia = Evidencia(
        descripcion="Nueva evidencia de problema persistente",
        fotos=[evidencia],
        fecha_registro=datetime.now()
    )


@step('describe el problema persistente "{descripcion}"')
def step_describir_problema(context, descripcion):
    context.descripcion_persistente = descripcion


@step('el reporte vuelve a "clasificando"')
def step_volver_clasificando(context):
    context.reporte.cambiar_estado(EstadoReporte.CLASIFICANDO)
    assert context.reporte.estado == EstadoReporte.CLASIFICANDO