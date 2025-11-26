#Descuento por edad
edad = int(input("ingrese su edad"))
if edad <0:
     print("edad no valida")
elif edad < 12:
     print("tiene un descuento del 30%")
elif edad < 18:
    print("tiene un descuento del 40%")
elif edad < 50:
      print("tiene un descuento del 90%")
else:
    print("no tiene descuento")