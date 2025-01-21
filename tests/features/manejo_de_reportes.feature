#Created by jona
#language: es

Característica: Manejar y gestionar problemas urbanos
  Como entidad publica,
  quiero clasificar , priorizar y gestionar los problemas reportados por los ciudadanos,
  para asignar recursos de manera eficiente y solucionar los problemas en el menor tiempo posible

  #Estados de los reportes
  #Clasificando
  #noAsignado
  #Asignado
  #Postergado
  #Resolviendo
  #Solucionado

  #---------- Clasificacion a Departamentos ----------
  Esquema del escenario: Clasificación automática de reporte ciudadano
    Dado un nuevo reporte ciudadano del problema "<descripcion_reporte>"
    Cuando el sistema encuentra coincidencias con el departamento "<departamento>"
    Y el nivel de confianza "<confianza>"% es mayor que 80%
    Entonces el reporte se clasifica como "asignado"
    Y se asigna al departamento "<departamento>"

    Ejemplos:
      | descripcion_reporte      | departamento       | confianza |
      | Bache en la calle        | Obras Públicas     | 95        |
      | Luminaria pública dañada | Alumbrado Público  | 90        |
      | Acumulación de basura    | Limpieza Pública   | 85        |
      | Árbol caído              | Parques y Jardines | 92        |

  Esquema del escenario: Fallo en clasificación automática
    Dado un nuevo reporte ciudadano del problema "<descripcion_reporte>"
    Cuando el sistema no puede determinar el departamento responsable ya que el nivel de confianza es menor a 80%
    Entonces el reporte se marca como "noAsignado"

    Ejemplos:
      | descripcion_reporte               |
      | Ruidos molestos intermitentes     |
      | Problema con vecino comerciante   |
      | Actividad sospechosa en el barrio |

  Esquema del escenario: Clasificación manual por coordinador
    Dado un reporte "noClasificado"
    Cuando el departamento de quejas asigna el departamento "<departamento>"
    Y registra la justificación "<justificacion>"
    Entonces el reporte cambia a "asignado"
    Y se añaden los nuevos criterios de clasificación

    Ejemplos:
      | departamento        | justificacion                              |
      | Fiscalización       | Requiere inspección por licencia comercial |
      | Seguridad Ciudadana | Necesita patrullaje y monitoreo            |
      | Desarrollo Social   | Caso requiere evaluación social            |

#-------- Atencion al problema --------
  Esquema del escenario: Inicio de atención del problema
    Dado un reporte "asignado" al departamento "<departamento>"
    Cuando el departamento tiene recursos disponibles
    Entonces el reporte cambia a "resolviendo"

    Ejemplos:
      | departamento      |
      | Obras Públicas    |
      | Alumbrado Público |
      | Limpieza Pública  |

  Esquema del escenario: Postergación de atención
    Dado un reporte "asignado"
    Cuando el departamento "<departamento>" no tiene recursos  disponibles
    Entonces el reporte cambia a "postergado"
    Y el departamento registra el motivo "<motivo>"
    Y el departamento establece una fecha estimada "<fecha_estimada>" para atender el reporte

    Ejemplos:
      | departamento       | motivo                            | fecha_estimada |
      | Obras Públicas     | Maquinaria en mantenimiento       | 3 días         |
      | Parques y Jardines | Personal en emergencia climática  | 2 días         |
      | Limpieza Pública   | Camiones en otra zona prioritaria | 1 día          |

  Esquema del escenario: Retomar problema postergado
    Dado un reporte "postergado"
    Cuando el departamento "<departamento>" tiene recursos disponibles
    Entonces el reporte cambia a "resolviendo"

    Ejemplos:
      | departamento     |
      | Obras Públicas   |
      | Limpieza Pública |

  Esquema del escenario: Resolución del problema ciudadano
    Dado un reporte en "resolviendo"
    Cuando el personal municipal registra:
      | acción realizada | "<accion>"    |
      | evidencia        | "<evidencia>" |
      | tiempo empleado  | "<tiempo>"    |
    Y adjunta fotos del trabajo realizado
    Entonces el reporte cambia a "solucionado"
    Y se solicita confirmación al ciudadano

    Ejemplos:
      | accion                  | evidencia             | tiempo  |
      | Reparación de bache     | Fotos antes y después | 5 horas |
      | Recolección de residuos | Foto área limpia      | 45 min  |
      | Poda de árbol           | Fotos del trabajo     | 2 horas |

  Esquema del escenario: Reapertura de reporte ciudadano
    Dado un reporte "solucionado"
    Cuando el ciudadano indica que el problema persiste
    Y proporciona nueva evidencia fotográfica "<evidencia>"
    Y describe el problema persistente "<descripcion>"
    Entonces el reporte vuelve a "clasificando"

    Ejemplos:
      | evidencia         | descripcion                               |
      | Foto de bache     | La reparación del bache se está hundiendo |
      | Foto de luminaria | La luz volvió a apagarse                  |
      | Foto de basura    | Siguen acumulando basura en el punto      |