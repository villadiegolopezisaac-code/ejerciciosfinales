#Raiz cuadrada posible
num = float(input("ingrese un numero para calcular su raiz cuadrada:"))
if num >= 0:
        raiz = num ** 0.5
        print("la raiz cuadrada de", num, "es" , raiz)
else:
        print(" no se puede calcular la raiaz cuadrada de un numero negativo")
