n = int(input("¿Cuántos empleados tiene la empresa?: "))
#creacion de lista para sueldos entre 1,000,000 y 3,000,000
sueldos_menor = []
#creacion de lista para sueldos mayores 3,000,000 y entre 5,000,000
sueldos_mayores = []

i = 0

while i < n:
    sueldo = float(input(f"Digite el sueldo del empleado {i + 1}: "))
    if 1000000 <= sueldo <= 5000000:
        if 1000000 <= sueldo <= 3000000:
            sueldos_menor.append(sueldo)
        elif 3000000 < sueldo <= 5000000:
            sueldos_mayores.append(sueldo)
    else:
        print("Sueldo no está en el rango permitido")
    i += 1

def totalsueldo(sueldos):
    return sum(sueldos)

print("Cantidad de sueldos entre 1,000,000 y 3,000,000:", len(sueldos_menor))
print("Cantidad de sueldos mayores 3,000,000 y entre 5,000,000:", len(sueldos_mayores))
print("Total de sueldos entre 1,000,000 y 3,000,000:", totalsueldo(sueldos_menor))
print("Total de sueldos mayores 3,000,000 y entre 5,000,000:", totalsueldo(sueldos_mayores))

