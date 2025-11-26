peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))

imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")