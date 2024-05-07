#contador = 0
#while contador < 10:
    #print (contador)
    #print("Hola")
    #contador = contador +1
    #contador += 1

import random

def jugar_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intento = int(input("¿Cuál crees que es? "))

        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
            break

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar_de_nuevo.lower() == "s":
        jugar_adivinanza()
    else:
        print("¡Gracias por jugar!")

jugar_adivinanza()
