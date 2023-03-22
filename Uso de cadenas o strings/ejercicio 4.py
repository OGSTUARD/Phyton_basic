def procesar_telefono(telefono):
    numero_sin_prefijo = telefono[4:14]
    numero_sin_ext = numero_sin_prefijo[:len(numero_sin_prefijo)-3]
    print(numero_sin_ext)
procesar_telefono("+1-809-691-6340")
