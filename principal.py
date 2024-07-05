import sqlite3

from funcionalidades.datos_juego.juego import juego_aleatorio
from funcionalidades.datos_juego.posciones import posciones



while True:
    print("""
          1. Jugar.
          2. Registro.
          3. Posiciones y puntuaciones.
          4. Salir.
          """)
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            juego_aleatorio()
        elif usuario == 4:
            print("Muchas gracias por jugar.")
            break
    except ValueError:
        print("El valor no es correcto, vuelve a digitar.")
        