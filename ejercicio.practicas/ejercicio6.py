h = int(input("Hora (0-23): "))
p = float(input("Precio: "))
if h < 12: d = 0.10
elif h >= 18: d = 0.20
else: d = 0
print("Total:", p - p*d)