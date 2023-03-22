n = int(input("Ingrese un número entero: "))

for i in range(1, n+1):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()
