#Created by jona
#language: es

Característica: Manejar los reportes ciudadanos
    Como entidad publica,
    quiero clasificar, atender y posponer los reportes enviados por los ciudadanos,
    para asignar recursos de manera eficiente y solucionar los problemas en el menor tiempo posible.

    #Estados de los reportes
        # no_asignado
        # asignado
        # postergado
        # resuelto

    Esquema del escenario: Resolver un reporte
        Dado un reporte ciudadano "id_reporte" del problema "<descripcion_problema>"
        Y su nivel de confianza de clasificacion es mayor que el 80% para cualquier departamento
        Y el reporte tiene el estado "<estado_reporte>"
        #asignado o postergado
        Cuando los recursos del departamento asignado sean necesarios para resolver el problema
        Entonces el estado del reporte cambia a "resuelto"
        Y el departamento debe registrar la evidencia de la solucion del reporte.
        Ejemplos:
            | descripcion_problema     | estado_reporte    |
            | Bache en la calle        | asignado          |
            | Luminaria pública dañada | postergado        |

    Escenario: Postergar reporte
        Dado un reporte ciudadano "id_reporte" del problema "descripcion_problema"
        Y su nivel de confianza de clasificacion es mayor que el 80% para cualquier departamento
        Cuando los recursos del departamento asignado no sean suficientes para resolver el problema
        Entonces el estado del reporte cambia a "postergado"
        Y el departamento

    Escenario: Asignacion manual
        Dado un reporte ciudadano "id_reporte" del problema "descripcion_problema"
        Y su nivel de confianza de clasificacion es menor que el 80% para cualquier departamento
        Cuando se realice una clasificacion manual al departamento "nombre_departamento"
        Entonces el estado del reporte cambia a "asignado"
        Y se añaden los nuevos criterios de clasificación
