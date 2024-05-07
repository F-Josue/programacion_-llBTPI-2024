

salir = False
Lista_compra = []

while not salir:
    print("------ Menu ------")
    print("1. Imprimir Listas De Compras")
    print("2. Agregar elementos a la lista")
    print("0. Salir")

    opt = input("Ingrese una opcion: ")

    if(opt == '0'):
        salir = True
    elif(opt == '1'):
        print("----------Lista de compras----------")
    
        for i in range(len(Lista_compra)):
           print(f"{i + 1}. {Lista_compra[i]}")
    elif(opt == '2'):
        nuevo_elemento = input("Inrese el nombre del producto: ")
        #print(nuevo_elemento)
        Lista_compra.append(nuevo_elemento)
        print (f"el elemento {nuevo_elemento} fue agregado a la lista")
    else:
         print("Opcion no valida")

#salir es booleano
#las listas se declaran con: [] (corchetes)