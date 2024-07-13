
# IMPORTAMOS "SQULITE3" PARA MANEJAR LA BASE DE DATOS

import sqlite3

# IMPORTAR "PANDAS" PARA VISUALIZAR LOS DATOS DE FORMA CLARA

import pandas as pd


# DEFINIR UNA FUNCION PARA USAR EN EL CODIGO PRINCIPAL

def jugador_puntuaciones():

    # CONECTAR CON LA BASE DE DATOS Y EL WITH CIERRA AUTOMATICAMENTE LA CONSULTA

    with sqlite3.connect("C:/Users/POWER/constructor_juego.db") as puntuaciones:

        # EL CURSOR ABRE LA CONSULTA Y MANJEA LA BASE DE DATOS

        consulta_cursor = puntuaciones.cursor()

        # CONSULTA QUE SELECCIONA LA TABLA DONDE SE VISUALIZAN LOS DATOS

        consulta_cursor.execute("SELECT * FROM Registro")

        # SE DEFINE EL METODO DE LECTURA
         
        resultado = consulta_cursor.fetchall()

    # SE USA EL METODO "DataFrame" PARA VISUALIZAR LA TABLA
    
    resultado_df = pd.DataFrame(resultado)

    # SE MUESTRA LA TABLA 
    
    print(resultado_df)