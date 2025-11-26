#Descuento por cantidad de compra
cantidad = int(input("ingrese la cantidad de productos comprados:"))
if cantidad >= 10:
    descuento = 20
    print("tiene un descuento del 20%")
elif cantidad >= 5:
    descuento = 10
    print("tiene un desccuento del 10%")
else:
    descuento = 0
    print("no tiene descuento")