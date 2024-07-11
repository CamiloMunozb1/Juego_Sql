
# IMPORTAMOS LA LIBRERIA "SQLITE3" PARA MANEJAR LA BASE DE DATOS

import sqlite3


# DEFINIR UNA FUNCION QUE SE PONDRA EN EL CODIGO PRINCIPAL 

def registro_usuario():

    # SE CONECTA A LA BASE DE DATOS, EL WITH CIERRA AUTOMATICAMENTE LA CONSULTA

    with sqlite3.connect("C:/Users/POWER/constructor_juego.db") as registro:
        try:

            # EL CURSOR ABRE LA CONSULTA Y MANJEA LA BASE DE DATOS

            consulta_cursor = registro.cursor()

            # ENTRADA DE USUARIO 

            registro_jugador = str(input("Ingresa tu alias o nombre de jugador: "))

            # ENTRADA DEL PUNTAJE DEL USUARIO

            puntaje_jugador = int(input("Ingresa tu puntaje en el juego: "))

            # CONSULTA QUE INGRESA EL DATO DEL USUARIO A LA BASE

            consulta_cursor.execute("INSERT INTO Registro (Jugador) VALUES (?)",(registro_jugador,))

            # CONSULTA QUE INGRESA EL PUNTAJE DEL USUARIO

            consulta_cursor.execute("INSERT INTO Registro (Puntaje) VALUES (?)",(puntaje_jugador,))

            # SE REALIZAN LOS CAMBIOS EN LA BASE

            registro.commit()

            # MENSAJE DE EXITO

            print("Datos añadidos correctamente.")

        # MANEJO DE ERRORES
        
        except ValueError:
            print("Valor no añadido ingrese una cadena de texto.")
        except sqlite3.Error as error:
            print(f"Fallo en la base de datos {error}")