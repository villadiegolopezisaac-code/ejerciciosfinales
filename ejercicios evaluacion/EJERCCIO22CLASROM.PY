lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comunes = []

for n in lista1:
    if n in lista2:
        comunes.append(n)

print(comunes)
