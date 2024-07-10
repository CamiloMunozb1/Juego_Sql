import random

def juego_aleatorio():
    numero_aleatorio = random.randint(1,11)
    numero = -1
    puntaje = 0
    seguir_jugandp = True

    while numero != numero_aleatorio:
        try:
            numero = int(input("Ingresa un numero: "))
            if numero == numero_aleatorio:
                puntaje += 10
                print(f"Muy bien el numero es {numero_aleatorio} y tu puntaje es {puntaje}")
                seguir_jugandp = False
            else:
                print(f"intenta de nuevo y tu puntaje es: {puntaje}")
            usuario = str(input("Deseas seguir jugando para sumar mas puntos? "))
            if usuario.lower() == "si":
                print("Comienza el juego")
                numero_aleatorio = random.randint(1,11)
            else:
                print("Saliendo del juego")
                seguir_jugandp = False
                break

        except ValueError:
            print("Error de digitacion, intenta de nuevo")
