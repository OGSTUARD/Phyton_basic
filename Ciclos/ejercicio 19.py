asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
notas = []

# Pedir la nota de cada asignatura al usuario
for asignatura in asignaturas:
    nota = float(input("Introduce la nota de {}:".format(asignatura)))
    notas.append(nota)

# Eliminar las asignaturas aprobadas
i = 0
while i < len(notas):
    if notas[i] >= 5:
        del notas[i]
        del asignaturas[i]
    else:
        i += 1

# Mostrar las asignaturas a repetir
print("Tienes que repetir las siguientes asignaturas:")
for asignatura in asignaturas:
    print(asignatura)
