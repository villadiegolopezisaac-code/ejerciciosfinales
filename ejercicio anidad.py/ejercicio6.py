edad = int(input("Edad: "))

if edad >= 18 and edad <= 70:
    print("Puede votar (obligatorio).")
elif edad > 70:
    print("Puede votar (opcional).")
else:
    print("No puede votar.")