# Desarrollo de steps y modelos relacionados con los escenarios
### Fecha: 04 enero del 2025 - 22 enero del 2025

## 1. Desarrollo en paralelo a los escenarios

El desarrollo de los **steps** se llevó a cabo de manera paralela a la definición de los escenarios en Gherkin. Esto permitió una integración ágil entre la especificación funcional y la implementación técnica, asegurando que cada escenario tuviera una ejecución clara dentro del sistema.

Se siguieron los siguientes pasos en el desarrollo:

1. **Definición de los escenarios en Gherkin**  
   - Se establecieron las acciones esperadas en cada escenario.
   - Se definieron las precondiciones y los resultados esperados.

2. **Identificación de los steps necesarios**  
   - Se analizaron los enunciados de los escenarios para extraer los pasos clave.
   - Se agruparon steps similares para evitar duplicación de código.

3. **Implementación de los steps en el framework de pruebas**  
   - Se utilizaron bibliotecas de automatización para la ejecución de los steps.
   - Se validaron las interacciones con los modelos de datos.

4. **Pruebas unitarias y de integración**  
   - Se verificó el correcto funcionamiento de cada step de manera individual.
   - Se realizaron pruebas de flujo completo con los escenarios definidos.

---

## 2. Desarrollo de los modelos necesarios

Para soportar la ejecución de los escenarios y steps, se implementaron los siguientes modelos dentro del sistema:

### **2.1. Modelo reporte**
El modelo `Reporte` representa las incidencias reportadas por los ciudadanos y su estado en el flujo de gestión.

**Atributos principales:**
- `id`: Identificador único del reporte.
- `descripcion`: Detalles del problema.
- `estado`: Estado actual del reporte (`no_asignado`, `asignado`, `postergado`, `resuelto`).
- `evidencia`: Archivos o imágenes como prueba de resolución.

### **2.2. Modelo departamento**
El modelo `Departamento` gestiona los equipos responsables de atender los reportes asignados.

**Atributos principales:**
- `nombre`: Nombre del departamento (ej. EPMMOP, Bomberos, Policía).
- `descripcion`: Descripcion detallada del departamento.

### **2.3. Modelo gestor de departamento**
El `Gestor de Departamento` es la entidad encargada de distribuir los reportes entre los departamentos correspondientes.

**Funciones principales:**
- **Recepción de reportes**: Procesa los reportes entrantes.
- **Asignación automática**: Determina a qué departamento debe ser enviado cada reporte.
- **Postergación de reportes**: Mueve reportes a estado `postergado` si no hay recursos disponibles.
- **Monitoreo del estado**: Actualiza el estado del reporte a medida que es atendido.

---
A continuacion se presentan los steps finales implementados:\
[Steps propuesta final](anexos.md#steps-propuesta-final)

