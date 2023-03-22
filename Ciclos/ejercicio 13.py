cantidad = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese la tasa de interés anual (%): "))
anios = int(input("Ingrese el número de años de la inversión: "))

capital = cantidad

for i in range(anios):
    capital += capital * (interes/100)
    print("Capital después del año", i+1, "es: ", round(capital, 2))
