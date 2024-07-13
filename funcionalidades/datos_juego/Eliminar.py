
# IMPORTAMOS "SQLITE3" PARA MANEJAR LA BASE DE DATOS

import sqlite3


# SE DEFINE UNA FUNCION PARA USARLA EN RL CODIGO ORIGINAL

def eliminar_jugador():

    # CONECTAR CON LA BASE DE DATOS Y EL WITH CIERRA AUTOMATICAMENTE LA CONSULTA

    with sqlite3.connect("C:/Users/POWER/constructor_juego.db") as eliminar_jugador:
        try:

            # EL CURSOR ABRE LA CONSULTA Y MANJEA LA BASE DE DATOS

            consulta_cursor =  eliminar_jugador.cursor()

            # ENTRADA DE USUARIO

            jugador_eliminar = str(input("ingresa el nombre del jugador: "))

            # CONSULTA QUE ELIMINA EL REGISTRO DEL NOMBRE DEL JUGADOR

            consulta_cursor.execute("DELETE FROM Registro WHERE Jugador = ?",(jugador_eliminar,))

            # EL REALIZA EL CAMBIO EN LA BASE DE DATOS

            eliminar_jugador.commit()

            # SE MUESTRA EL MENSAJE DE EXITO

            print("Jugador eliminado")

        # MANEJO DE ERRORES
        
        except ValueError:
            print("Error de digitacion intenta de nuevo")

