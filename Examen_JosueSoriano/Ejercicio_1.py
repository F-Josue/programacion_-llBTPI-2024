salir = False

while not salir:
    print("------ Menu ------")
    print("1. Comprobar numero")
    print("0. Salir")

    opt = input("Ingrese una opcion: ")

    if(opt == '0'):
        salir = True
    elif(opt == '1'):
        numero = int(input("ingrese un numero: "))
    
    if(numero % 2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
else:
    print("Opcion no valida")









    #resultado = 2+2 == 0
    #print(f"{resultado} es par")

    #resultado = 1+1 == 0
    #print(f"{resultado} es impar")
    #resultado += 1