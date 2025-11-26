m = float(input("Monto: "))
s = float(input("Saldo: "))
print("Fraude" if m > s*0.8 else "Transacción normal")