# **Estimación de Features**
La estimación de los Features se la realizó de la siguiente forma:
1. En el tablero Kanban, una vez definidos los Features, por cada uno de ellos se establece una estimación.
2. La estimación se evalua y se itera si es necesario.

## **1. Primera propuesta de estimación**
La primera estimación se realizó utilizando la técnica de Planning Poker que consiste en:
1. Todos los integrantes del equipo participan en la estimación de cada feature o historia de usuario.
2. Cada integrante elige un número de la serie de Fibonacci (1, 2, 3, 5, 8, 13, 21, etc.), que representa el **esfuerzo** y el **tiempo** necesario para desarrollar la funcionalidad.
3. Los votos se revelan simultáneamente y, si hay discrepancias significativas, se discuten hasta llegar a un consenso y  se itera.

Siguiendo esos pasos se obtuvo la siguiente estimación:

|Nº| **Feature** | **Estimación** |
|--|------------|------------------------|
|1| Reportar problemas urbanos en la ciudad | 13 |
|2| Manejar y gestionar problemas urbanos | 5 |
|3| Consultar el estado y condiciones de mi zona | 5 |
|4| Reservar espacios públicos | 8 |
|5| Crear eventos públicos masivos | 5 |
|6| Suscribirse a canales de interés | 8 |
|7| Reservar asistencia a eventos comunitarios | 5 |
|| **Total**| **49** |

## **2. Segunda propuesta de estimación**
Para refinar la estimación de los features se usa la misma técnica, Planning Poker, pero se cambia el enfoque de la estimación. Ahora ya no se considera el esfuerzo y el tiempo, se define la estimación con base en: 
- **Complejidad**: Nivel de complejidad ciclomática que tiene el implementar el feature.  
- **Incertidumbre**: Grado de conocimiento o riesgos asociados a su implementación.  

Así, se obtiene la segunda estimación, y final, de los features:


|Nº| **Feature** | **Estimación final** |
|--|------------|---------------------|
|1| Reportar problemas urbanos en la ciudad | 2 |
|2| Manejar y gestionar problemas urbanos | 1 |
|3| Consultar el estado y condiciones de mi zona | 1 |
|4| Reservar espacios públicos | 2 |
|5| Crear eventos públicos masivos | 2 |
|6| Suscribirse a canales de interés | 2 |
|7| Reservar asistencia a eventos comunitarios | 1 |
|8| **Total** | **11** |

---
## 3. Anexos
Para evidenciar la metodología y técnicas aplicadas para la estimacion de los features se presenta el siguiente anexo, en donde las estimaciones están escritas bajo cada Feature.

[Anexo de Features](anexos.md#kanban-de-features)

