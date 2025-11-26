a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Sí pueden formar un triángulo")
else:
    print("NO pueden formar un triángulo")