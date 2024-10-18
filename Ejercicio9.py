'''Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa
 y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también 
 funcione cuando el día o el mes se introduzcan con un solo carácter. '''

fecha = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: \n")
fechasep = fecha.split("/")
print("Naciste el dia", fechasep[0], "del mes", fechasep[1], "del año", fechasep[2])