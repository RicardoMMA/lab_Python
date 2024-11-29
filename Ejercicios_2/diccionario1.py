estudiantes = {}

n = int(input("Ingrese el número de estudiantes: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    estudiantes[nombre] = calificacion

print("\nDiccionario de estudiantes y sus calificaciones:")
for nombre, calificacion in estudiantes.items():
    print(f"Estudiante: {nombre}, Calificación: {calificacion}")

mejor_estudiante = max(estudiantes, key=estudiantes.get)
print(f"\nEl estudiante con la calificación más alta es {mejor_estudiante} con una calificación de {estudiantes[mejor_estudiante]}")

while True:
    print("\n--- Actualización de datos ---")
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    
    calificacion = float(input(f"Ingrese la nueva calificación de {nombre}: "))
    if nombre in estudiantes:
        print(f"Actualizando calificación de {nombre}...")
    else:
        print(f"Añadiendo nuevo registro para {nombre}")
    estudiantes[nombre] = calificacion

    print("\nDiccionario actualizado de estudiantes y sus calificaciones:")
    for nombre, calificacion in estudiantes.items():
        print(f"Estudiante: {nombre}, Calificación: {calificacion}")

