cadena = "banana"
conteo = {}

for letra in cadena:
    if letra in conteo:
        conteo[letra] += 1
    else:
        conteo[letra] = 1

print(conteo)
