import random

def juego_aleatorio():
    numero_aleatorio = random.randint(1,11)
    numero = -1
    puntaje = 0
    while numero != numero_aleatorio:
        try:
            numero = int(input("Ingresa un numero: "))
            if numero == numero_aleatorio:
                puntaje += 10
                print(f"Muy bien el numero es {numero_aleatorio} y tu puntaje es {puntaje}")
                break
            else:
                print(f"intenta de nuevo y tu puntaje es: {puntaje}")

        except ValueError:
            print("Error de digitacion, intenta de nuevo")
