from menu import imprimir_menu
from datos import crear_tarea, obtener_todas_las_tareas
import json

salir = True


with open('test.json') as f:
    texto = f.read()
    print(texto)

    data = json.loads(texto)
    print(data)
    print(data['usuarios'][0]['id'])
    
    
    
    
    
    
    
    
    
    
    
    
while not salir:
    imprimir_menu()
    resp = input("Ingrese una opcion: ")
    
    if resp == '0':
        salir = True
    elif resp == '1':
        print('\n-----Todas las tareas------')
        tareas = obtener_todas_las_tareas()
        for tarea in tareas:
            index = tareas.index(tarea)
            print(f'{index + 1}. {tarea['titulo']}')
            
    elif resp == '2':
        pass
    elif resp == '3':
        pass
    elif resp == '4':
        titulo_tarea = input('Ingrese la nueva tarea: ')
        crear_tarea(titulo_tarea)
        print('\n¡Tarea Agregada!\n\n')
    elif resp == '5':
        pass
    else:
        print(f'la opcion "{resp}" no es valida.')