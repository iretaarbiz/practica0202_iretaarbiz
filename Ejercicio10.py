'''Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta. '''

lista = input("Introduce los productos de tu lista de la compra separados por comas: \n")
listasep = lista.split(", ")
for i in range(len(listasep)):
    print(listasep[i])