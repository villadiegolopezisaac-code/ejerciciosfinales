p = float(input("Precio: "))
tipo = input("Es esencial? (si/no): ")
iva = 0.05 if tipo=="si" else 0.19
print("Total:", p + p*iva)