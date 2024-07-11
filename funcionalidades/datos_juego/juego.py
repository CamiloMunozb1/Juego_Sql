
# SE IMPORTA LA LIBRERIA "RANDOM" PARA OBTENER UN NUMERO LEATORIO

import random


# DEFINIR UNA FUNCION QUE SE PONDRA EN EL CODIGO PRINCIPAL 

def juego_aleatorio():

    # USUAMOS UNA VARIABLE QUE TOME UN NUMERO ALEATORIO DEL 1 AL 11

    numero_aleatorio = random.randint(1,11)

    # USUAMOS UN NUMERO NEGATIVO PARA ESTABLECER UNA DIFERENCIA CON EL NUMERO ALEATORIO

    numero = -1

    # USAMOS LA VARIABLE "CONTADOR" PARA CONTAR EL PUNTAJE DEL USUARIO

    puntaje = 0

    # CON LA VARUABLE "SEGUIR_JUGANDO" VERIFICAMOS SI EL USUARIO DESEA SEGUIR EN EL JUEGO

    seguir_jugandp = True

    # VERIFICAMOS SI LA VARIABLE "NUMERO" Y "NUMERO_AEATORIO" SON DIFERENTES

    while numero != numero_aleatorio:

        try:

            # ENTRADA DE USUARIO

            numero = int(input("Ingresa un numero: "))

            # EN ESTA CONDICION VERIFICAMOS SI LA ENTRADA DEL USUARIO ES IGUAL AL "NUMERO_ALEATORIO"

            if numero == numero_aleatorio:

                # SI EL USUARIO ACIERTA SE SUMA AL CONTADOR 10 PUNTOS

                puntaje += 10

                # Y SE IMPRIME UN MENSAJE DE FELICITACION

                print(f"Muy bien el numero es {numero_aleatorio} y tu puntaje es {puntaje}")

                # SI EL USUARIO DECIDE SEGUIR JUGANDO USUAMOS LA VARIABLE "SEGUIR_JUGANDO"

                seguir_jugandp = False

            else:

                # SI EL USUARIO NO ADIVINA EL NUMERO NO SE SUMAN PUNTOS AL CONTADOR Y SE IMPRIME EL SIGUIENTE MENSAJE

                print(f"intenta de nuevo y tu puntaje es: {puntaje}")

            # SE PREGUNTA AL USUARIO SI DESEA SEGUIR JUGANDO

            usuario = str(input("Deseas seguir jugando para sumar mas puntos? "))

            # EN UNA CONDICION VERIFICAMOS SI LA RESPUESTA DEL USUARIO ES POSITIVA Y SE GENERA UN NUEVO NUMERO

            if usuario.lower() == "si":
                print("Comienza el juego")
                numero_aleatorio = random.randint(1,11)

            # SI LA RESPUESTA ES NEGATIVA SE SALE DEL JUEGO Y SE CIERRA EL PROBLEMA

            else:
                print("Saliendo del juego")
                seguir_jugandp = False
                break

        # MANEJO DE ERRORES

        except ValueError:
            print("Error de digitacion, intenta de nuevo")
