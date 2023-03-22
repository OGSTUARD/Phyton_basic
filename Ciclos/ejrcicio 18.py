asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
notas = []

# Pedir la nota de cada asignatura al usuario
for asignatura in asignaturas:
    nota = float(input("Introduce la nota de {}:".format(asignatura)))
    notas.append(nota)

# Mostrar las notas de cada asignatura
for i in range(len(asignaturas)):
    print("En {} has sacado {}".format(asignaturas[i], notas[i]))
