ingredientes = {"vegetariana": ["mozzarella", "tomate", "pimiento", "tofu"], 
                "no vegetariana": ["mozzarella", "tomate", "peperoni", "jamón", "salmón"]}

tipo_pizza = input("¿Quiere una pizza vegetariana? (s/n): ")
if tipo_pizza == "s":
    tipo_pizza = "vegetariana"
elif tipo_pizza == "n":
    tipo_pizza = "no vegetariana"
else:
    print("Opción no válida")
    exit()

print(f"Ingredientes disponibles para pizza {tipo_pizza}:")
for i, ingrediente in enumerate(ingredientes[tipo_pizza]):
    print(f"{i + 1}. {ingrediente}")

opcion = int(input("Elige un ingrediente (introduce el número): "))
if opcion not in range(1, len(ingredientes[tipo_pizza]) + 1):
    print("Opción no válida")
    exit()

ingredientes_elegidos = [ingredientes[tipo_pizza][0], ingredientes[tipo_pizza][opcion]]
print(f"La pizza elegida es {tipo_pizza} y lleva los siguientes ingredientes: {', '.join(ingredientes_elegidos)}")
