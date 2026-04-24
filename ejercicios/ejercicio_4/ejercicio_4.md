# Ejercicio 4: Actualizando posiciones con map y lambda

Todos los enemigos retroceden 10 píxeles. Usa `map` y `lambda` para restarle 10 a cada coordenada de la lista original.
```python
# Tu tarea:
coordenadas = [50, 80, 200, 400]
# nuevas_coordenadas = list(map(...))
```

> **Ejemplo Guía:** (Aumentar el daño de cada ataque usando map y lambda)
> ```python
> atq_base = [10, 15, 20]
> # Le decimos: por cada elemento "atq", devuelve "atq + 10"
> atq_aumentados = list(map(lambda atq: atq + 10, atq_base)) 
> print(atq_aumentados) # Resultado: [20, 30, 40]
> ```
