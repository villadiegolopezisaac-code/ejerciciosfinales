#Crea un programa que pida la edad de una persona y determine la edad determine si es un niño (0-12 años), un adolescente (13-17 años), un adulto (18-64 años) o un adulto mayor (65 años omás).
lista=["edades de personas entre 12 y 65 años"]
num = int(input("ingrese su edad: "))
for i in range(1):
    if num >=0 and num <=12:
        print("es un niño")
    elif num >=13 and num <=17:
        print("es un adolescente")
    elif num >=18 and num <=64:
        print("es un adulto")
    elif num >=65:
        print("es un adulto mayor")
    else:
        print("edad no valida"
              )