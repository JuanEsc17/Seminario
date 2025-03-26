rules = """Respeta a los demás. No se permiten insultos ni lenguaje
 ofensivo.
 Evita el spam. No publiques enlaces sospechosos o repetitivos.
 No compartas información personal.
 Usa los canales adecuados para cada tema.
 Sigue las instrucciones de los moderadores."""

#Solicita palabra clave al usuario
palabra = input("Ingrese una palabra clave: ")

#Busca la palabra clave en las reglas e imprime la regla que la contiene
for word in rules.split('\n'):
    if palabra in word:
        print(word)
