# **Validación del proceso de verificación del desarrollo de software usando BDD**

## 1. **Contexto del proyecto**
- **Nombre del proyecto:** App for City Services  
- **Business challenge:**  
  Desarrollar una aplicación que permita a los ciudadanos comunicarse con instituciones municipales para reportar problemas, recibir información local y participar en actividades comunitarias.  

---
## 2. Verificación de features
### 2.1. **Primer acercamiento a los features**
Los **features** se derivaron del análisis del Business Challenge del proyecto. Estos son los features que inicialmente fueron identificados:

1. **Reportar problemas de la ciudad**  
Como ciudadano,
quiero reportar problemas urbanos (como grafitis, señales ilegales, o infraestructura dañada) en mi localidad,    
para que los servicios municipales puedan ser notificados y se tomen acciones correctivas.
2. **Realizar actividades grupales**  
Como ciudadano,    
quiero crear actividades grupales o eventos comunitarios (como reservar una cancha o organizar una iniciativa de caridad),    
para que otros ciudadanos puedan unirse a la actividad o evento.
3. **Integracion de 311**  
Como ciudadano,    
quiero acceder al servicio 311    
para registrar solicitudes o reportes sobre servicios municipales no relacionados con emergencias.
4. **Monitorear las solicitudes de solución de problemas**  
Como ciudadano,    
quiero hacer un seguimiento de las solicitudes que he enviado sobre problemas,    
para conocer el progreso y estado de las solicitudes.
5. **Reservar asistencia eventos de la comunidad**  
Como ciudadano,    
quiero reservar mi lugar en eventos publicos  que ocurren en mi barrio  
para participar activamente en los mismos.
6. **Suscripcion a canales de interés**  
Como ciudadano,  
quiero suscribirme a canales de noticias locales o temas de mi interés,  
para mantenerme informado acerca de novedades de mi barrio.
7. **Informar anuncios importantes**  
Como municipalidad,  
quiero publicar anuncios importantes dirigidos a la ciudadanía  
para que ellos estén informados sobre eventos, avisos o decisiones relevantes. 

### 2.2. **Analisis de los features iniciales**
La verificación de estos features se realizó mediante un workshop con los compañeros del equipo, quienes aportaron su perspectiva sobre:
- La **relevancia** de cada feature respecto a los objetivos del proyecto.  
- El cumplimiento de los **criterios de calidad** y de los criterios **INVEST**.
- La **priorización** de los features más importantes en función del impacto y el valor que genera esta solución en el negocio.  

De los features que se obtuvieron del Business Challenge solo se pudieron tomar los que cumplen con el método ***INVEST*** y los atributos de calidad ***(correctitud, completitud, exactitud, consistencia, testeabilidad y legibilidad)***. Ademas, fue necesario realizar algunas modificaciones a algunos features. Así se obtuvo que:

- El feature **2** se modificó para que ahora aborde el problema de reservar espacios públicos.
- El feature **4** se une al feature **1** ya que son parte del mismo problema y así se cumpliria la Independencia de ***INVEST***.
-El feature **3** es una instancia del feature **1** ya que no interesa el cómo se realiza la acción si no que importa qué se realiza.
- La prioridad en que se presentan los features tambien es importante ya que se refleja el valor que entrega al negocio.

### 2.3 **Features corregidos**

De esta forma, se presentan los *nuevos* features organizados por prioridad y manteniendo los **criterios de calidad** e **INVEST**:

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


## 3. **Estimación de features**
### 3.1. **Primera estimación de features**
La primera estimación fue por **story points fibonacci** basado en la *experiencia* de los miembros del grupo. Considerando el nivel de dificultad y el tiempo que tomaria completarlo. 
De esta forma se obtuvo la siguiente tabla de estimación:
#### Tabla de estimación

| **Feature**                               | **Estimación** |
|-------------------------------------------|---------------:|
| Reportar problemas urbanos en la ciudad   | 13            |
| Manejar y gestionar problemas urbanos     | 5             |
| Consultar el estado y condiciones de mi zona | 5          |
| Reservar espacios públicos                | 8             |
| Crear eventos públicos masivos            | 5             |
| Suscribirse a canales de interés          | 8             |
| Reservar asistencia a eventos comunitarios | 5            |



### 3.2. Analisis de la estimacion de los features
Una estimación correcta debe ser independiente de las habilidades técnicas de los involucrados en el desarrollo.
Por ello la estimación de cada feature se realizó en base a:  
- **Complejidad**: Nivel de complejidad ciclomática que tiene el implementar el feature.  
- **Incertidumbre**: Grado de conocimiento o riesgos asociados a su implementación.  

De igual manera, se utilizó la **Escala de Fibonacci** para realizar la estimación: `1, 2, 3, 5, 8, 13, 21, 34, 55`

#### Tabla de estimación
| **Feature**                               | **Estimación** |
|-------------------------------------------|---------------:|
| Reportar problemas urbanos en la ciudad   | 2              |
| Manejar y gestionar problemas urbanos     | 1             |
| Consultar el estado y condiciones de mi zona | 1          |
| Reservar espacios públicos                | 2             |
| Crear eventos públicos masivos            | 2             |
| Suscribirse a canales de interés          | 2             |
| Reservar asistencia a eventos comunitarios | 1            |
|                                           |11             |
