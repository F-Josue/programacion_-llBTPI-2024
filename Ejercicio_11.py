#Solicitar el nombre de usuario y guardarlo en una variable llamada "nota_usuario"
#Si la variable "nota_usuario" es mayor a 70:
#Imprimir por consola el texto "has aprobado"
#Caso contrario
#Imprimir por consola el texto "has reprobado"

#Codigo

nota_usuario = int(input("ingrese su nota: "))
if(nota_usuario > 70):
    print("aprobado")
else:
    print("desaprobado")