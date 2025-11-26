a = int(input("Primer número: "))
b = int(input("Segundo número: "))

if b != 0 and a % b == 0:
    print(f"{a} es múltiplo de {b}")
else:
    print(f"{a} NO es múltiplo de {b}")