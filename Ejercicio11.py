'''Escribir un programa que pregunte el nombre el un producto, su precio y un número 
de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su
precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos
y el coste total con 8 dígitos enteros y 2 decimales. '''

producto = input("Producto: \n")
precio = float(input("Precio: \n"))
unidades = int(input("Unidades: \n"))
total = round(precio, 2) * unidades
print("El producto {} vale {:9.2f} y quiero {:3d} unidades. El total es de {:8}€".format(producto, precio, unidades, round(total, 2)))