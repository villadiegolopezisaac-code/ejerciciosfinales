letra = input("Ingresa una letra: ").lower()

if letra in "aeiou":
    print("Es vocal")
elif letra.isalpha() and len(letra) == 1:
    print("Es consonante")
else:
    print("Entrada inválida")