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


    Escenario: Resolver reportes asignados a un departamento
        Dado los siguientes reportes ciudadanos llegan al departamento "SIAC"
          | id_reporte | descripcion_reporte           |
          | R001       | Basura y escombros en la calle asfalto| #Revisar
          | R002       | Bache en la vía principal     |
          | R003       | Drenaje bloqueado por basura  |
        Y los reportes han sido asignados automáticamente a un departamento
        Cuando el departamento "EMASEO" priorice los reportes asignados
        Y el departamento atienda el reporte "R001"
        Entonces el departamento registra la evidencia "Basura recogida" de la solución del reporte atendido
        Y el estado del reporte atendido cambia a "resuelto"


    Escenario: Resolver reportes postergados de un departamento
        Dado los siguientes reportes ciudadanos llegan al departamento "SIAC"
          | id_reporte | descripcion_reporte           |
          | R001       | Luminaria pública dañada      |
          | R002       | Bache en la vía principal     |
          | R003       | Drenaje bloqueado por basura  |
        Y los reportes han sido asignados automáticamente a un departamento
        Y el departamento posterga el reporte "R002"
        Cuando el departamento atienda el reporte "R002"
        Entonces el departamento registra la evidencia "Se ha rellenado el bache" de la solución del reporte atendido
        Y el estado del reporte atendido cambia a "resuelto"


    Escenario: Asignación manual de reportes no clasificados
        Dado los siguientes reportes ciudadanos llegan al "SIAC"
          | id_reporte | descripcion_reporte           |
          | R001       | Luminaria pública dañada      |
          | R002       | Bache en la vía principal     |
          | R003       | Drenaje bloqueado por basura  |
        Y los reportes no han sido asignados automáticamente a ningún departamento
        Cuando se realiza una asignación manual del reporte "R003" al departamento "EPMMOP"
        Entonces el estado del reporte asignado cambia a "asignado"
        Y se añaden los siguientes criterios de clasificación para el departamento asignado:
          | criterio    |
          | bache       |
          | poste       |
          | banqueta    |