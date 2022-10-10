'''

Opción1
Lista para nombres
Lista para telefonos


Opción 2:
Lista para nombres y telefonos

Ejemplo[Juan - Teléfono, Pepe - Teléfono]
'''

#Opción 1:
from curses.ascii import VT


vNombres = []
vTelefonos = []

Nombre=(input("Dime un nombre:\n"))
Tele=(input("Dime su teléfono:\n"))

vNombres.append(Nombre)
vTelefonos.append(Tele)

print(vNombres)
print(vTelefonos)