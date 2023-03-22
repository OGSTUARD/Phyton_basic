def asignar_grupo():
    nombre = input("Introduce tu nombre: ")
    sexo = input("Introduce tu sexo (M/F): ")
    grupo = ""
    if (sexo == "M" and nombre.lower() > "n") or (sexo == "F" and nombre.lower() < "m"):
        grupo = "A"
    else:
        grupo = "B"
    print(f"Tu grupo es: {grupo}")
asignar_grupo()
