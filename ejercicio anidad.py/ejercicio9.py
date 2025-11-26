cat = input("Categoría (A-E): ").upper()
monto = float(input("Monto: "))

descuentos = {"A":0.30, "B":0.20, "C":0.10, "D":0.05, "E":0}

desc = descuentos.get(cat, 0)
total = monto * (1 - desc)

print("Total a pagar:", total)
