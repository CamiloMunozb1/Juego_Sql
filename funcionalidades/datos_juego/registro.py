import sqlite3

def registro_usuario():
    with sqlite3.connect("C:/Users/POWER/constructor_juego.db") as registro:
        try:
            consulta_cursor = registro.cursor()
            registro_jugador = str(input("Ingresa tu alias o nombre de jugador: "))
            consulta_cursor.execute("INSERT INTO Registro (Jugador) VALUES (?)",(registro_jugador,))
            registro.commit()
            print("Datos añadidos correctamente.")
        except ValueError:
            print("Valor no añadido ingrese una cadena de texto.")
        except sqlite3.Error as error:
            print(f"Fallo en la base de datos {error}")