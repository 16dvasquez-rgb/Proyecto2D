# Ejercicio 3: Encontrar cerca del jugador

Dada una lista de posiciones en X de varios enemigos, crea una nueva lista vacía y guarda ahí SOLO los números que sean mayores a 100 y menores a 150.
```python
# Tu tarea:
posiciones_x = [80, 110, 200, 140, 50, 145]
enemigos_cerca = []
# Escribe aquí tu lógica...
```

> **Ejemplo Guía:** (Guardar en una nueva lista solo los precios entre $10 y $20)
> ```python
> precios = [5, 15, 25, 18, 12, 30]
> precios_medios = []
> for p in precios:
>     if p > 10 and p < 20: # O también: if 10 < p < 20:
>         precios_medios.append(p)
> print(precios_medios) # Resultado: [15, 18, 12]
> ```
