#imprimir la primera y la ultima palabra letra de cada palabra en una frase. frase ="Este es un ejemplo"
frase = "este es un ejemplo"
palabras = frase.split()
for palabra in palabras:
    print("Primera letra:", palabra[0], "Ultima letra:", palabra[-1])
