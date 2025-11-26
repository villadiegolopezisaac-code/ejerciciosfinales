ingreso = float(input("Ingreso anual: "))

if ingreso <= 10000:
    impuesto = ingreso * 0.05
elif ingreso <= 20000:
    impuesto = ingreso * 0.10
elif ingreso <= 35000:
    impuesto = ingreso * 0.15
else:
    impuesto = ingreso * 0.20

print("Impuesto a pagar:", impuesto)