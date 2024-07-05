import random

def juego_aleatorio():
    numero_aleatorio = random.randint(1,11)
    numero = -1
    while numero != numero_aleatorio:
        try:
            numero = int(input("Ingresa un numero: "))
            if numero == numero_aleatorio:
                print(f"Muy bien el numero es {numero_aleatorio}")
                break
            else:
                print("intenta de nuevo")

        except ValueError:
            print("Error de digitacion, intenta de nuevo")
