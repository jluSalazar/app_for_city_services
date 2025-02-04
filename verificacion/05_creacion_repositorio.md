# Proyecto django

# Creación del repositorio en GitHub para la aplicación en Django

## 1. Configuración del repositorio

Para gestionar el código fuente de la aplicación en **Django**, se creó un repositorio en **GitHub** con la siguiente configuración:

1. Se accedió a GitHub y se creó un nuevo repositorio con un nombre representativo para la aplicación ``servicios-ciudadanos``.
2. Se definió la visibilidad del repositorio, asegurando que fuera accesible solo para los colaboradores autorizados en caso de ser privado.
3. Se inicializó el repositorio con un archivo de documentación `README.md` donde se detallaron los pasos para instalar las dependencias y una plantilla de `.gitignore` específica para **Django** y el IDE PyCharm.
4. Se establecieron los permisos adecuados para los miembros del equipo, permitiendo contribuciones según su rol en el proyecto.

---

## 2. Definición de estándares de programación

**Fecha de reunión:** 24/10/24, 21:34  
**Objetivo:** Definir estándares de programación y flujo de trabajo colaborativo.

Durante la reunión del equipo, se establecieron estándares de programación para asegurar la calidad y mantenibilidad del código:

- Se adoptó un estándar de estilo de código para **Python PEP8**, promoviendo la claridad y coherencia en la escritura del código.
   1. **Uso de Snake Case (`snake_case`)**  
      - Se estableció el uso de `snake_case` para nombres de variables y funciones, asegurando legibilidad y alineación con las mejores prácticas en **Python**.
      - Ejemplo: `numero_reporte = 12345`, `asignar_departamento()`

   2. **Uso de Camel Case (`CamelCase`)**  
      - Se aplicará `CamelCase` únicamente para nombres de **clases** y modelos dentro del framework Django.
      - Ejemplo: `class ReporteMunicipal(models.Model)`
   3. **Variables y funciones descriptivas**  
      - Los nombres de variables deben ser **claros y específicos**, evitando abreviaciones innecesarias.
      - Se prohíbe el uso de nombres genéricos como `x`, `temp`, `data`, a menos que su significado sea evidente en el contexto.
- Se acordó realizar **revisiones de código obligatorias** para cada contribución antes de ser integrada en la rama principal (develop).

---

## 3. Estrategia de branching para trabajo colaborativo

Para permitir un desarrollo estructurado y colaborativo, se implementó una estrategia de **branching**, estableciendo las siguientes reglas:

1. Se definió una **rama principal** destinada únicamente para versiones estables y listas para producción.
2. Se creó una **rama de desarrollo (develop)** en la que se integran y prueban cambios antes de ser fusionados en la principal.
3. Se estableció que cada nueva funcionalidad o corrección de errores debe desarrollarse en una **rama separada (feature)**, siguiendo una convención de nombres para facilitar su identificación.
4. Se promovió la práctica de fusionar cambios mediante **Pull Requests (PRs)**, asegurando la revisión y validación del código antes de su integración.
5. Se acordó que las ramas que ya han sido fusionadas y no sean necesarias sean eliminadas para mantener un repositorio ordenado.


---


## 4. Reglas para Pull Requests (PRs)

Para garantizar un proceso estructurado en la revisión y validación del código, se establecieron las siguientes reglas para los **Pull Requests (PRs):**

1. **Convención en la nomenclatura de PRs**  
   - Todos los PRs deben seguir un formato estándar en su título para facilitar su identificación y comprensión.

2. **Validación mediante pruebas automáticas**  
   - Antes de aprobar cualquier PR, es obligatorio que pase exitosamente todas las pruebas de **Behave**, asegurando que el código no introduzca fallos en la aplicación.

3. **Control de calidad del código con SonarQube**  
   - Se implementó un **Quality Gate** que analiza el código en busca de errores, problemas de seguridad y duplicaciones. Solo los PRs que cumplan con los estándares de calidad pueden ser aprobados.


---

## 5. Integración y despliegue continuo (CI/CD)

Para automatizar el proceso de validación del código y asegurar un desarrollo ágil, se implementaron herramientas de **Integración y Despliegue Continuo (CI/CD)** a través de **GitHub Actions**:

1. Se configuró un flujo de trabajo automatizado para ejecutar pruebas de **Behave** cada vez que se crea o actualiza un PR.
2. Se implementó un análisis automático de calidad de código con **SonarQube**, asegurando que el código cumpla con los estándares definidos.
3. Se estableció un mecanismo de validación que bloquea la fusión de PRs si no cumplen con los criterios de calidad y pruebas exitosas.
4. Se creó una estructura de reportes de validación que permite a los desarrolladores revisar el estado de sus PRs antes de la aprobación.

Evidencia de llos workflows de los CI:\
[Script ci.yml](anexos.md#ciyml-github)