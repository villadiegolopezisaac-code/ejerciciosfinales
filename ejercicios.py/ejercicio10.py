#calculadora basica
num1 = float(int(input("ingrese el primer numero:")))
num2 = float(int(input("ingrese el segundo numero:")))
operacion =input("ingrese la operacion que desea realizar (+,-,*/)")
if operacion == "+":
    resultado = num1 + num2
    print("el resultado de la suma es:", resultado)
elif operacion == "-":
    resultado = num1 - num2
    print("el resultado de la resta es:", resultado)
elif operacion == "*":
    resultado= num1 * num2
    print("el resultado de la multiplicacion es:", resultado)
elif operacion == "/":
     resultado = num1 / num2
     print("el resultado de la division es:", resultado)