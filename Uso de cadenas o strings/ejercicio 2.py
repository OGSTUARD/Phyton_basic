def imprimir_nombre_completo(nombre_completo):
    # Imprimir el nombre completo en minúsculas
    print(nombre_completo.lower())

    # Imprimir el nombre completo en mayúsculas
    print(nombre_completo.upper())

    # Imprimir el nombre completo con la primera letra de cada palabra en mayúsculas
    palabras = nombre_completo.split()
    nombre_formateado = " ".join([palabra.capitalize() for palabra in palabras])
    print(nombre_formateado * 3)
    
imprimir_nombre_completo("Kenny Bueno")
    
