import sqlite3
import pandas as pd

def jugador_puntuaciones():
    with sqlite3.connect("C:/Users/POWER/constructor_juego.db") as puntuaciones:
        consulta_cursor = puntuaciones.cursor()
        consulta_cursor.execute("SELECT * FROM Registro")
        resultado = consulta_cursor.fetchall()
    resultado_df = pd.DataFrame(resultado)
    print(resultado_df)