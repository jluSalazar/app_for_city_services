# Verificación de Features
## **1. Primera propuesta de Features**
Cada uno de los *squads* tuvo la tarea de definir 7 features los cuales deben ser derivados del análisis del *business challenge* del proyecto mediante la **metodología de análisis documental**, la cual consiste en extraer información relevante de documentos con el fin de interpretar su contenido, encontrar datos y generar conocimiento. 
Con base en la información recopilada se identificaron los siguientes Features:

1. **Reportar problemas de la ciudad**  
   **Como** ciudadano,  
   **quiero** reportar problemas urbanos (como grafitis, señales ilegales o infraestructura dañada) en mi localidad,  
   **para que** los servicios municipales puedan ser notificados y se tomen acciones correctivas.  

2. **Realizar actividades grupales**  
   **Como** ciudadano,  
   **quiero** crear actividades grupales o eventos comunitarios (como reservar una cancha o organizar una iniciativa de caridad),  
   **para que** otros ciudadanos puedan unirse a la actividad o evento.  

3. **Integración de 311**  
   **Como** ciudadano,  
   **quiero** acceder al servicio 311  
   **para** registrar solicitudes o reportes sobre servicios municipales no relacionados con emergencias.  

4. **Monitorear las solicitudes de solución de problemas**  
   **Como** ciudadano,  
   **quiero** hacer un seguimiento de las solicitudes que he enviado sobre problemas,  
   **para** conocer el progreso y estado de las solicitudes.  

5. **Reservar asistencia en eventos de la comunidad**  
   **Como** ciudadano,  
   **quiero** reservar mi lugar en eventos públicos que ocurren en mi barrio  
   **para** participar activamente en los mismos.  

6. **Suscripción a canales de interés**  
   **Como** ciudadano,  
   **quiero** suscribirme a canales de noticias locales o temas de mi interés,  
   **para** mantenerme informado acerca de novedades de mi barrio.  

7. **Informar anuncios importantes**  
   **Como** municipalidad,  
   **quiero** publicar anuncios importantes dirigidos a la ciudadanía  
   **para que** ellos estén informados sobre eventos, avisos o decisiones relevantes.  

## 1.1. Evaluacion de los features
Una vez definida la primera propuesta de los features se evaluaron los mismos utilizando los criterios de calidad y el método **INVEST**, mediante un *workshop* con el equipo de desarrollo. Se evaluó:
- La **relevancia** de cada feature.  
- El **cumplimiento de criterios de calidad** (correctitud, completitud, exactitud, consistencia, testeabilidad y legibilidad).  
- La **independencia de los Features** en función de INVEST.  

| **Número** | **Feature** | **Relevancia** | **Criterios de calidad** | **INVEST** | **Observaciones** |
|-----------|------------|---------------|--------------------------------------|---------|-------------------|
| 1 | Reportar problemas de la ciudad | ✅ | ✅ | ✅ | Es el problema principal que resuelve la aplicación |
| 2 | Realizar actividades grupales | ✅ | ❌ | ✅ | Le falta precisión, se enfoca el problema a la reserva de espacios públicos |
| 3 | Integración de 311 | ❌ | ❌ | ❌ | Fuera del alcance del proyecto |
| 4 | Monitorear las solicitudes de solución de problemas | ✅ | ❌ | ❌ | Falta de indeoendencia, se relaciona con el **Feature 1** |
| 5 | Reservar asistencia en eventos de la comunidad | ✅ | ✅ | ✅ |  |
| 6 | Suscripción a canales de interés | ✅ | ✅ | ✅ |  |
| 7 | Informar anuncios importantes | ❌ | ❌ | ❌ | No está alineado con la solucion del problema |

---

## **2. Segunda propuesta de Features**
Una vez evaluados los Features de la primera propuesta se establecen nuevos features con mejoras en calidad y priorización. 
La metodología usada fue el contraste de los Features mediante un **Kanban** entre los grupos de trabajo.
1. Se estableció un tablero Kanban con columnas representando cada uno de los squads participantes.
2. A cada squad se le asignó un color específico, especificamente, el squad 6 utilizó el color gris.
3. Cada squad analizó su contexto y listó los features encontrados en su respectiva columna del Kanban.
4. Se revisaron los features de todos los equipos para identificar:
   - Duplicaciones (features similares en varios squads).
   - Posibles mejoras o combinaciones de features para mayor impacto.
   - Features que podrían ser descartados por falta de valor.
5. Se seleccionaron los features con mayor valor, marcándolos en el tablero.
6. Se consolidó una lista de features finales, reduciendo redundancias y asegurando su alineación con los objetivos del proyecto.
 
De esta forma, se obtuvieron los siguientes Features para el proyecto.

1. **Reportar problemas urbanos en la ciudad**  
**Como** ciudadano,  
**quiero** reportar problemas urbanos en mi localidad<!-- utilizando imágenes, descripción y ubicación,   -->  
**para que** los servicios municipales sean notificados y tomen acciones correctivas rápidamente.

2. **Manejar y gestionar problemas urbanos**   
**Como** entidad pública,  
**quiero** clasificar, priorizar y gestionar los problemas reportados por los ciudadanos,  
**para** asignar recursos de manera eficiente y solucionar los problemas en el menor tiempo posible.

3. **Consultar el estado y condiciones de mi zona**   
**Como** ciudadano,  
**quiero** ver un resumen del estado actual de mi zona en términos de problemas, actividades y eventos,  
**para** estar informado y participar activamente en mi comunidad.

4. **Reservar espacios públicos**  
**Como** ciudadano,  
**quiero** reservar espacios públicos como parques, canchas deportivas o salones comunales,  
**para** organizar actividades o eventos sin conflictos de horarios.

5. **Crear eventos públicos masivos**  
**Como** municipalidad,  
**quiero** crear y publicar eventos públicos masivos,  
**para que** los ciudadanos participen activamente en ellos.

6. **Suscribirse a canales de interés**  
**Como** ciudadano,  
**quiero** suscribirme a canales temáticos o noticias locales de mi interés,  
**para** recibir notificaciones personalizadas sobre lo que sucede en mi barrio.

7. **Reservar asistencia a eventos comunitarios**   
**Como** ciudadano,  
**quiero** reservar mi lugar en eventos públicos organizados en mi barrio o ciudad,  
**para** confirmar mi asistencia y participar activamente en actividades comunitarias.

Luego de definir la segunda propuesta de los Features (y la propuesta final) se evaluan cada uno de los criterios evaluados anteriormente:

| **Número** | **Feature** | **Relevancia** | **Cumplimiento de criterios de calidad** | **INVEST** |
|-----------|------------|---------------|--------------------------------------|---------|
| 1 | Reportar problemas urbanos en la ciudad | ✅ | ✅ | ✅ | 
| 2 | Manejar y gestionar problemas urbanos | ✅ | ✅ | ✅ | 
| 3 | Consultar el estado y condiciones de mi zona | ✅ | ✅ | ✅ | 
| 4 | Reservar espacios públicos | ✅ | ✅ | ✅ | 
| 5 | Crear eventos públicos masivos | ✅ | ✅ | ✅ | 
| 6 | Suscribirse a canales de interés | ✅ | ✅ | ✅ | 
| 7 | Reservar asistencia a eventos comunitarios | ✅ | ✅ | ✅ |
---
## 3. Asignación de Features
Cada uno de estos Features se han asignado a los squads. En el caso del grupo 6 se le asignó el Feature 2. Manejar y gestionar problemas urbanos.

---
## 3. Anexos
Para evidenciar la metodología y técnicas aplicadas para la definicion de los features se presenta el siguiente anexo.

[Anexo de Features](anexos.md#kanban-de-features)

