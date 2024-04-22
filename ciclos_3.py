

salir = False

while not salir:
    print("------ Menu ------")
    print("1. Suma")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Division")
    print("0. Salir")

    opt = input("Ingrese una opcion: ")

    if(opt == '0'):
        salir = True
    elif(opt == '1'):
        numero1 = int(input("ingrese un numero: "))
        numero2 = int(input("ingrese otro numero: "))

        resultado = numero1 + numero2
        
        print("El resutado es: " + str(resultado))
    elif(opt == '2'):
        numero1 = int(input("ingrese un numero: "))
        numero2 = int(input("ingrese otro numero: "))

        resultado = numero1 - numero2
        
        print("El resutado es: " + str(resultado))
    elif(opt == '3'):
        numero1 = int(input("ingrese un numero: "))
        numero2 = int(input("ingrese otro numero: "))

        resultado = numero1 * numero2
        
        print("El resutado es: " + str(resultado))
    elif(opt == '4'):
        numero1 = int(input("ingrese un numero: "))
        numero2 = int(input("ingrese otro numero: "))

        resultado = numero1 / numero2
        
        print("El resutado es: " + str(resultado))

