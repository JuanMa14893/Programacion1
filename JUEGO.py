#hacer un juego donde 2 jugadores, jugador 1 y jugador 2 tengan una palabra, 
#uno tendrá consonantes y otro vocales de la palabra escogida
#Se define ganador el que mas combinaciones tenga
#hecho por Juan Manuel Londoño 1004734441


def obtener_subcadenas(palabra, usar_vocales):
    vocales = "AEIOUaeiou"
    resultado = []

    for i in range(len(palabra)):
        letra = palabra[i]

        if (usar_vocales and letra in vocales) or (not usar_vocales and letra not in vocales):
            for j in range(i + 1, len(palabra) + 1):
                subcadena = palabra[i:j]
                resultado.append(subcadena)
    return resultado

palabra = input("Escribe la palabra para jugar: ")

jugador_A = obtener_subcadenas(palabra, usar_vocales=True)

jugador_B = obtener_subcadenas(palabra, usar_vocales=False)

print("\nJugador A (vocales):", jugador_A)
print("Cantidad:", len(jugador_A))

print("\nJugador B (consonantes):", jugador_B)
print("Cantidad:", len(jugador_B))

print("\nResultado del juego:")
if len(jugador_A) > len(jugador_B):
    print("Gana el Jugador A")
elif len(jugador_B) > len(jugador_A):
    print("Gana el Jugador B")
else:
    print("Empate")