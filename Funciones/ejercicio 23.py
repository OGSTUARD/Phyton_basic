def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def palabra_mas_repetida(frecuencia):
    max_frecuencia = 0
    palabra_max_frecuencia = None
    for palabra, freq in frecuencia.items():
        if freq > max_frecuencia:
            max_frecuencia = freq
            palabra_max_frecuencia = palabra
    return (palabra_max_frecuencia, max_frecuencia)
