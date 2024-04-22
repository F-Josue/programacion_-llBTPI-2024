sueldo_usuario = int(input("ingrese su sueldo: "))
if(sueldo_usuario < 7000):
    print("no debe pagar impuestos")
else:
     i = sueldo_usuario
print("debe pagar: ")
print (f"{0.08*i}")      
print("de impuestos")