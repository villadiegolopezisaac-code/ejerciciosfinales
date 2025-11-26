horas = float(input("Horas trabajadas: "))
paga = float(input("Pago por hora: "))

if horas > 40:
    extra = horas - 40
    salario = 40 * paga + extra * paga * 1.5
else:
    salario = horas * paga

print("Salario total:", salario)