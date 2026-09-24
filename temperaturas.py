def rango_temperaturas(lista_temperaturas):
    minima = min(lista_temperaturas)
    maxima = max(lista_temperaturas)
    return (minima, maxima)
lecturas_motor = [45, 20, 78, 85, 32, 60]

minima, maxima = rango_temperaturas(lecturas_motor)

print(f"Temperatura mínima: {minima}°C")
print(f"Temperatura máxima: {maxima}°C")
