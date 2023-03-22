def verificar_contraseña(contraseña):
    contraseña_usuario = input("Introduce la contraseña: ")
    if contraseña.lower() == contraseña_usuario.lower():
        print("La contraseña es correcta")
    else:
        print("La contraseña es incorrecta")
verificar_contraseña("klk11")
