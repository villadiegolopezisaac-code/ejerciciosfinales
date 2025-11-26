usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("Usuario: ")
clave = input("Contraseña: ")

if usuario == usuario_correcto and clave == contrasena_correcta:
    print("Acceso concedido")
else:
    print("Usuario o contraseña incorrectos")