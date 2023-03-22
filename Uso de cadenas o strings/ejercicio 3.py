def contar_letras(nombre):
    nombre_mayusculas = nombre.upper()
    n_letras = len(nombre)
    mensaje = f"{nombre_mayusculas} tiene {n_letras} letras"
    print(mensaje)
contar_letras("kennys")
