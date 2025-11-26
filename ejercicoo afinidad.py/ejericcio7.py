a = float(input("Número 1: "))
b = float(input("Número 2: "))

if abs(100 - a) < abs(100 - b):
    print(f"{a} está más cerca de 100")
elif abs(100 - a) > abs(100 - b):
    print(f"{b} está más cerca de 100")
else:
    print("Ambos están igual de cerca de 100")