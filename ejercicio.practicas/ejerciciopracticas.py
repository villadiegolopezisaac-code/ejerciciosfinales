pwd = input("Contraseña: ")

may = False
minu = False
num = False

for c in pwd:
    if c >= 'A' and c <= 'Z':
        may = True
    elif c >= 'a' and c <= 'z':
        minu = True
    elif c >= '0' and c <= '9':
        num = True

if may and minu and num:
    print("Contraseña válida")
else:
    print("Contraseña inválida")