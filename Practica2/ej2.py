titles = [
 "Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
 "Jugando al nuevo FPS del momento con amigos",
 "Música en vivo: improvisaciones al piano"
 ]

#Busco el titulo mas largo
longest_title = ""
for title in titles:
    if len(title) > len(longest_title):
        longest_title = title
print("El título más largo es: "+longest_title)