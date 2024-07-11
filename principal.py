
# LLAMADA A LAS FUNCIONES PARA USARLAS POR MEDIO DE FUNCIONES

from funcionalidades.datos_juego.juego import juego_aleatorio
from funcionalidades.datos_juego.registro import registro_usuario
from funcionalidades.datos_juego.Puntuaciones import jugador_puntuaciones
from funcionalidades.datos_juego.Eliminar import  eliminar_jugador


while True:

    # MENU DEL USUARIO

    print("""
          1. Jugar.
          2. Registro.
          3. jugadores y puntuaciones.
          4. Eliminar jugador.
          5. Salir.
          """)
    try:

        # ENTRADA DEL USUARIO

        usuario = int(input("Ingresa una opcion: "))

        # CONDICIONES DEPENDIENDO DE LA ENTRADA DEL USUARIO

        if usuario == 1:
            juego_aleatorio()
        elif usuario == 2:
            registro_usuario()
        elif usuario == 3:
            jugador_puntuaciones()
        elif usuario == 4:
            eliminar_jugador()
        elif usuario == 6:
            print("Muchas gracias por jugar.")
            break
    
    # MANEJO DE PROBLEMAS
    
    except ValueError:
        print("El valor no es correcto, vuelve a digitar.")
         