n1 = float(input("Nota parcial 1: "))
n2 = float(input("Nota parcial 2: "))
n3 = float(input("Examen final: "))

prom = (n1 + n2 + n3) / 3
print(f"Promedio: {prom}")

if prom >= 60:
    print("Aprobado")
else:
    print("Reprobado")