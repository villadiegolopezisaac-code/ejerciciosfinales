c = input("Código: ")
p = float(input("Precio: "))
d = 0.20 if c=="DESC20" else 0.10 if c=="DESC10" else 0
print("Total:", p - p*d)