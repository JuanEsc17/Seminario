import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    ("// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario"),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Inicializo puntaje
puntaje = float(0) 

# Genero pack de preguntas y respuestas
question_pack = list(zip(questions, answers, correct_answers_index))

#

# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question, answer_choices, correct_index = random.choice(question_pack)
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answer_choices):
        print(f"{i + 1}. {answer}")
    
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1
            if user_answer < 0 or user_answer >= len(answer_choices):
                print("Respuesta no valida")
                sys.exit(1)
        except ValueError:
            print("Respuesta no valida")
            sys.exit(1)
            
    # Se verifica si la respuesta es correcta 
        if user_answer == correct_index:
            print("¡Correcto!")
            puntaje += 1
            break
        else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
            if intento == 0:
                print("Incorrecto")
            else:
                print("Incorrecto. La respuesta correcta es:")
                print(answer_choices[correct_index])
            puntaje -= 0.5
    # Se imprime un blanco al final de la pregunta
    print()
print("Tu puntaje es")
print(puntaje)