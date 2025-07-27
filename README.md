# Algoritmo Voraz - Organizador de Actividades

Este script implementa un **algoritmo voraz** para organizar una agenda diaria de actividades sin traslapes. Su objetivo es seleccionar el mayor número posible de actividades que no se encimen entre sí, priorizando las que terminan más temprano.

## 📌 Descripción del problema

Dado un conjunto de actividades con una hora de inicio, una hora de fin y una descripción, se busca crear una agenda ideal seleccionando las actividades que se pueden realizar sin conflictos de horario.

Ejemplo de entrada:
```python
actividades = [
    (9.00, 10.5, 'Gym'),
    (9.5, 10.5, 'Almuerzo'),
    (11.5, 12.5, 'Clase'),
    (12.5, 13.5, 'Super'),
    (11.00, 13.5, 'Preparar comida'),
    (14.00, 15.5, 'Clase de yoga'),
    (13.00, 14.5, 'Estudio')
]
