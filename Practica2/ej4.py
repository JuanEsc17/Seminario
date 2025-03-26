#Solicito nombre de usuario
usuario = input("Ingrese su nombre de usuario: ")

#Verifico que tenga al menos 5 caracteres, un numero, una letra mayuscula y solo letras y numeros
if len(usuario) < 5:
    print("El nombre de usuario no cumple con los requisitos")
elif not any(char.isdigit() for char in usuario):
    print("El nombre de usuario no cumple con los requisitos")
elif not any(char.isupper() for char in usuario):
    print("El nombre de usuario no cumple con los requisitos")
elif not usuario.isalnum():
    print("El nombre de usuario no cumple con los requisitos")
else:
    print("El nombre de usuario es valido")