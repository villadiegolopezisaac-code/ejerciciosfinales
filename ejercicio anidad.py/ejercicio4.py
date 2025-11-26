print("1) Suma  2) Resta  3) Multiplicación  4) División")

op = int(input("Elige operación: "))
a = complex(float(input("Real 1: ")), float(input("Imaginario 1: ")))
b = complex(float(input("Real 2: ")), float(input("Imaginario 2: ")))

if op == 1:
    r = a + b
elif op == 2:
    r = a - b
elif op == 3:
    r = a * b
elif op == 4:
    if b == 0:
        print("Error: división por cero")
        exit()
    r = a / b
else:
    print("Opción inválida")
    exit()

print("Resultado:", r)