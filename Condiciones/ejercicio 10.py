def evaluar_empleado():
    puntos = float(input("Introduce la puntuación del empleado: "))
    nivel = ""
    if puntos == 6:
        nivel = "Inaceptable"
    elif puntos == 10:
        nivel = "Aceptable"
    elif puntos >= 15:
        nivel = "Meritorio"
    cantidad = 2400 * puntos
    print(f"El nivel de rendimiento del empleado es {nivel} y recibirá {cantidad}€.")
evaluar_empleado()