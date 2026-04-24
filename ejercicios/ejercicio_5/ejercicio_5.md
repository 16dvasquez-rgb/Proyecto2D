# Ejercicio 5: Clases Básicas

1. Crea una clase `Jugador`.
2. En su constructor (`__init__`), inicializa un atributo `puntos` en 0.
3. Crea un método llamado `sumar_puntos(self, cantidad)` que le sume la `cantidad` a los puntos actuales.
```python
# Tu tarea:
# class Jugador:
#     ...
```

> **Ejemplo Guía:** (Clase Coche que suma kilometraje)
> ```python
> class Coche:
>     def __init__(self):
>         self.kilometraje = 0
>         
>     def conducir(self, km_recorridos):
>         self.kilometraje += km_recorridos
> 
> # Uso:
> mi_auto = Coche()
> mi_auto.conducir(50)
> print(mi_auto.kilometraje) # Resultado: 50
> ```
