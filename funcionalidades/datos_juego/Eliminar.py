import sqlite3

def eliminar_jugador():
    with sqlite3.connect("C:/Users/POWER/constructor_juego.db") as eliminar_jugador:
        try:
            consulta_cursor =  eliminar_jugador.cursor()
            jugador_eliminar = str(input("ingresa el nombre del jugador: "))
            consulta_cursor.execute("DELETE FROM Registro WHERE Jugador = ?",(jugador_eliminar,))
            eliminar_jugador.commit()
            print("Jugador eliminado")
        except ValueError:
            print("Error de digitacion intenta de nuevo")

