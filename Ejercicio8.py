'''Escribir un programa que pregunte por consola el precio de un producto en 
euros con dos decimales y muestre por pantalla el número de euros y el número
de céntimos del precio introducido. '''

precio = input("Introduce el precio de un producto con dos decimales: \n")
preciosep = precio.split(".")
print("El producto vale", preciosep[0], "euros y", preciosep[1], "céntimos.")
