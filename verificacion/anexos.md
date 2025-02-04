# Anexos de verificación
## Kanban de Features
![Tablero Kanban](./photos/Fetures.png)

## Escenarios primera propuesta
```gherkin
Esquema del escenario: Escenario: Atender reporte notificado
    Dado un empleado público "<nombre_empleado>" está trabajando en el sistema
    Y el estado "<estado_actual>" del reporte "<nombre_reporte>" es por revisar o postergado
    Cuando se cambia el estado del reporte "<nombre_reporte>" a por atender
    Entonces se envia una notificación al equipo de atención correspondiente "<departamento>" para inciar el proceso de solución del reporte
    Y notifica al ciudadano "<nombre_ciudadano>" que el problema será tratado inmediatamente



     Ejemplos: Reportes críticos
    | nombre_empleado | nombre_reporte          | estado_actual  | departamento                     | nombre_ciudadano |
    | Juan Pérez      | Fuga de agua            | por revisar    | Departamento de Obras            | Marcela          |
    | María Gómez     | Corte de electricidad   | postergado     | Departamento de Energía          | Carlos           |
    | Lucía Martínez  | Bache en carretera      | por revisar    | Departamento de Transporte       | Julio            |
    | Pedro López     | Problema de alumbrado   | postergado     |  Departamento de Infraestructura | Andres           |

  Esquema del escenario: Escenario:  Postergar reporte notificado
    Dado un empleado público "<nombre_empleado>" está trabajando en el sistema
    Y el estado "<estado_actual>" del reporte "<nombre_reporte>" es por revisar
    Cuando se cambia el estado del reporte "<nombre_reporte>" a postergado
    Entonces se muestra una notificación después de "<dias>" días definidos por el empleado para recordarle revisar el reporte postergado
    Y notifica al ciudadano "<nombre_ciudadano>" que el problema será tratado según la disponibilidad de recursos

    Ejemplos: Reportes con prioridad baja
    | nombre_empleado | nombre_reporte           | estado_actual | dias | nombre_ciudadano|
    | Luis Mejía      | Ruido en el vecindario   | por revisar   | 5    | Ana             |
    | Elena Torres    | Contenedor lleno         | por revisar   | 3    | Mario           |
    | Francisco Vega  | Árbol caído en parque    | por revisar   | 7    | Laura           |
    | Marta Cruz      | Basura en la acera       | por revisar   | 2    | Jaime           |

  Esquema del escenario: Denegar reporte notificado
  Dado un empleado público "<nombre_empleado>" está trabajando en el sistema
    Y el estado "<estado_actual>" del reporte "<nombre_reporte>" es por revisar
    Cuando se cambia el estado del reporte "<nombre_reporte>" a denegado
    Entonces se notifica al ciudadano "<nombre_ciudadano>"  que el reporte no se encuentra bajo la jurisdicción de la institución pública

    Ejemplos: Reportes fuera de jurisdicción
    | nombre_empleado | nombre_reporte            | estado_actual | nombre_ciudadano|
    | Carolina Ramos  | Corte de internet         | por revisar   | Fernando        |
    | Andrés Silva    | Servicio telefónico caído | por revisar   | Adriana         |
    | Rosa Díaz       | Problema con cableado TV  | por revisar   | Javier          |
    | Daniel Ortega   | Entrega de correspondencia| por revisar   | Luisa           |

```

## Proceso de manejo de reportes
![Sketch del proceso de manejo de reportes](./photos/proceso_manejo_reportes.jpeg)

## Escenarios segunda propuesta
```gherkin
Esquema del escenario: Clasificación automática de reporte ciudadano
    Dado un nuevo reporte ciudadano
    Cuando el sistema analiza el problema reportado "<descripcion_reporte>"
    Y encuentra coincidencias con el departamento "<departamento>"
    Y el nivel de confianza es "<confianza>"%
    Entonces el reporte se clasifica como "asignado"
    Y se asigna al departamento "<departamento>"

    Ejemplos:
      | descripcion_reporte         | departamento       | confianza |
      | Bache en la calle           | Obras Públicas     | 95        |
      | Luminaria pública dañada    | Alumbrado Público  | 90        |
      | Acumulación de basura       | Limpieza Pública   | 85        |
      | Árbol caído                 | Parques y Jardines | 92        |

  Esquema del escenario: Fallo en clasificación automática
    Dado un nuevo reporte ciudadano con problema "<problema>"
    Cuando el sistema no puede determinar el departamento responsable ya que el nivel de confianza es menor a 80%
    Entonces el reporte se marca como "noClasificado"
    Y requiere revisión del coordinador municipal

    Ejemplos:
      | problema                          |
      | Ruidos molestos intermitentes     |
      | Problema con vecino comerciante   |
      | Actividad sospechosa en el barrio |

  Esquema del escenario: Clasificación manual por coordinador
    Dado un reporte "noClasificado"
    Cuando el coordinador municipal asigna el departamento "<departamento>"
    Y registra la justificación "<justificacion>"
    Entonces el reporte cambia a "asignado"
    Y el sistema aprende los criterios de clasificación

    Ejemplos:
      | departamento          | justificacion                               |
      | Fiscalización         | Requiere inspección por licencia comercial  |
      | Seguridad Ciudadana   | Necesita patrullaje y monitoreo            |
      | Desarrollo Social     | Caso requiere evaluación social             |

  Esquema del escenario: Inicio de atención del problema
    Dado un reporte "asignado" al departamento "<departamento>"
    Cuando el departamento tiene personal disponible
    Entonces el reporte cambia a "resolviendo"
    Y se notifica al ciudadano

    Ejemplos:
      | departamento       |
      | Obras Públicas     |
      | Alumbrado Público  |
      | Limpieza Pública   |

  Esquema del escenario: Postergación de atención
    Dado un reporte "asignado"
    Cuando el departamento "<departamento>" no tiene recursos disponibles
    Entonces el reporte cambia a "postergado"
    Y se registra el motivo "<motivo>"
    Y se comunica nueva fecha estimada "<fecha_estimada>"

    Ejemplos:
      | departamento      | motivo                           | fecha_estimada|
      | Obras Públicas    | Maquinaria en mantenimiento      | 3 días        |
      | Parques y Jardines| Personal en emergencia climática | 2 días        |
      | Limpieza Pública  | Camiones en otra zona prioritaria| 1 día         |

  Esquema del escenario: Retomar problema postergado
    Dado un reporte "postergado"
    Cuando el departamento "<departamento>" tiene recursos disponibles
    Entonces el reporte cambia a "resolviendo"
    Y se notifica al ciudadano el inicio de trabajos

    Ejemplos:
      | departamento     |
      | Obras Públicas   |
      | Limpieza Pública |

  Esquema del escenario: Resolución del problema ciudadano
    Dado un reporte en "resolviendo"
    Cuando el personal registra:
      | acción realizada  | "<accion>"     |
      | evidencia         | "<evidencia>"   |
      | tiempo empleado   | "<tiempo>"      |
    Y adjunta fotos del trabajo realizado
    Entonces el reporte cambia a "solucionado"
    Y se solicita confirmación al ciudadano

    Ejemplos:
      | accion                    | evidencia                | tiempo    |
      | Reparación de bache      | Fotos antes y después    | 5 horas   |
      | Recolección de residuos  | Foto área limpia         | 45 min    |
      | Poda de árbol            | Fotos del trabajo        | 2 horas   |

  Esquema del escenario: Reapertura de reporte ciudadano
    Dado un reporte "solucionado"
    Cuando el ciudadano indica que el problema persiste
    Y proporciona nueva evidencia fotográfica "<evidencia>"
    Y describe el problema persistente "<descripcion>"
    Entonces el reporte vuelve a "clasificando"

    Ejemplos:
      | evidencia              | descripcion                               |
      | Foto de bache         | La reparación del bache se está hundiendo |
      | Foto de luminaria     | La luz volvió a apagarse                  |
      | Foto de basura        | Siguen acumulando basura en el punto      |
    
```
## Escenario propuesta final
```gherkin
Característica: Manejar los reportes ciudadanos
    Como entidad publica,
    quiero clasificar, atender y posponer los reportes enviados por los ciudadanos,
    para asignar recursos de manera eficiente y solucionar los problemas en el menor tiempo posible.


    Escenario: Resolver reportes asignados a un departamento
        Dado nuevos reportes que llegan al gestor de departamentos
        | nombre     | correo              | identificacion | asunto       | descripcion | ubicacion | cantidad_registro | prioridad |
        | Juan Perez | juan.perez@test.com | 1727263717     | inundacion   | Se inundo   | Av. 123   | 13                | 1         |
        | Juan Perez | juan.perez@test.com | 1727263717     | incendio     | Se inundo   | Av. 123   | 8                 | 2         |
        Y los reportes han sido asignados automáticamente a un departamento
        Y los reportes son priorizados por su asunto
        Cuando el departamento "EPMMOP" atienda el reporte "1"
        Entonces el departamento registra la evidencia "Basura recogida" de la solución del reporte atendido
        Y el estado del reporte atendido cambia a "resuelto"


    Escenario: Resolver reportes postergados de un departamento
        Dado nuevos reportes que llegan al gestor de departamentos
        Y el departamento "EPMMOP" posterga el reporte "2"
        Cuando el departamento "EPMMOP" atienda el reporte "2"
        Entonces el departamento registra la evidencia "Se ha rellenado el bache" de la solución del reporte atendido
        Y el estado del reporte atendido cambia a "resuelto"
```

## Steps propuesta final
```gherkin
"""
Este módulo contiene los pasos definidos para las pruebas de comportamiento
utilizando Behave.
"""
from behave import *

from app.Reporte import Reporte
from app.GestorDeDepartamentos import GestorDeDepartamentos
from app.Departamento import Departamento


#use_step_matcher("re")

#Escenario 1.1
@step('los siguientes reportes ciudadanos llegan al gestor de departamentos')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.gestor_de_departamentos = GestorDeDepartamentos()

    context.gestor_de_departamentos = GestorDeDepartamentos()
    for row in context.table:
        reporte = Reporte(row["id_reporte"], row["descripcion_reporte"])
        context.gestor_de_departamentos.agregar_nuevo_reporte_no_asignado(reporte)
    pass



@step('los reportes han sido asignados automáticamente a un departamento')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    context.gestor_de_departamentos.asignar_automaticamente_reportes_a_departamentos()
    pass


@step('el departamento "{nombre_departamento}" priorice los reportes asignados')
def step_impl(context, nombre_departamento):
    """
    :type nombre_departamento: str
    :type context: behave.runner.Context
    """
    context.departamento = context.gestor_de_departamentos.obtener_departamento_por_nombre(nombre_departamento)
    context.departamento.priorizar_reportes()
    pass


@step('el departamento atienda el reporte "{id_reporte_atendido}"')
def step_impl(context, id_reporte_atendido):
    """
    :type id_reporte_atendido: str
    :type id_reporte_atendido: str
    :type context: behave.runner.Context
    """
    context.reporte_atendido = context.departamento.obtener_reporte_por_id(id_reporte_atendido)
    context.departamento.atender_reporte(context.reporte_atendido)
    assert "atendiendo" == context.reporte_atendido.obtener_estado() , "El reporte no está siendo atendido"


@step("el departamento registra la evidencia {descripcion_evidencia} de la solución del reporte atendido")
def step_impl(context, descripcion_evidencia):
    """
    :type descripcion_evidencia: str
    :type context: behave.runner.Context
    """
    context.departamento.registrar_evidencia(context.reporte_atendido, descripcion_evidencia)
    assert "" != context.reporte_atendido.obtener_evidencia(), \
        "El reporte {context.reporte_atendido.obtener_id()} no tiene la evidencia registrada."


@step('el estado del reporte atendido cambia a "resuelto"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.reporte_atendido.cambiar_estado("resuelto")
    assert context.reporte_atendido.obtener_estado() == "resuelto", \
        f"El estado del reporte {context.reporte_atendido.obtener_id()} no se actualizó correctamente."

#Escenario 2.1
@step('el departamento "{nombre_departamento}" posterga el reporte "{id_reporte_postergado}"')
def step_impl(context, nombre_departamento, id_reporte_postergado):
    """
    :param nombre_departamento:
    :type id_reporte_postergado: str
    :type context: behave.runner.Context
    """
    context.departamento = context.gestor_de_departamentos.obtener_departamento_por_nombre(nombre_departamento)
    context.reporte_postergado = context.departamento.obtener_reporte_por_id(id_reporte_postergado)
    context.departamento.postergar_reporte(context.reporte_postergado)
    assert context.reporte_postergado.obtener_estado() == "postergado", \
        f"El estado del reporte {context.reporte_postergado.obtener_id()} no se actualizó correctamente."


#Escenrio 3.1
@step('los reportes no han sido asignados a ningún departamento')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    reportes_no_asignados = context.gestor_de_departamentos.obtener_reportes_no_asignados()
    assert len(reportes_no_asignados) > 0, "Todos los reportes han sido asignados automáticamente."

@step('se realiza una asignación manual del reporte "{id_reporte}" al departamento "{departamento}"')
def step_impl(context, id_reporte, departamento):
    """
    :type id_reporte: str
    :type departamento: str
    :type context: behave.runner.Context
    """

    reporte_no_asignado = context.gestor_de_departamentos.obtener_reporte_por_id(id_reporte)

    departamento_destino = context.gestor_de_departamentos.obtener_departamento_por_nombre(departamento)

    if not departamento_destino:
        departamento_destino = Departamento(departamento)
        context.gestor_de_departamentos.agregar_departamento(departamento_destino)

    context.gestor_de_departamentos.asignar_manualmente_reporte_a_departamento(reporte_no_asignado, departamento_destino)
    context.departamento = departamento_destino
    context.reporte_asignado = reporte_no_asignado

    assert context.reporte_asignado in context.departamento.obtener_reportes_asignados(), \
    "El reporte no fue asignado correctamente al departamento."

@step('el estado del reporte asignado cambia a "asignado"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.reporte_asignado.obtener_estado() == "asignado", \
        f"El reporte {context.reporte_asignado.obtener_id()} no cambió a estado 'asignado'."

@step('se añaden los siguientes criterios de clasificación para el departamento asignado')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    criterios = [row["criterio"] for row in context.table]
    context.gestor_de_departamentos.agregar_criterios_clasificacion_por_departamento(context.departamento, criterios)
    for criterio in criterios:
        assert criterio in context.gestor_de_departamentos.obtener_criterios_clasificacion_por_departamento(context.departamento), \
            f"El criterio '{criterio}' no fue añadido correctamente al departamento '{context.departamento}'."
```