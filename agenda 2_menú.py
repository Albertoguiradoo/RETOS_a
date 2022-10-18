#menú
''''
1-Insertar Contacto 
2-Borrar contacto
3-Buscar contacto
4- Ver todos los contactos
5- Salir
'''
def pintaMenú():
    opc = 0
    while(opc<1 or opc >5 ):
        print("Pulse 1 para insertar Contacto ")
        print("Pulse 2 para borrar contacto")
        print("Pulse 3 para buscar contacto")
        print("Pulse 4 para ver todos los contactos")
        print("Pulse 5 para salir")
        try :
            opc= int(input("Dime una opción: \n"))
        except:
            print("Las opciones son de la 1 a la 5.Por favor, intentelo de nuevo")
    
    return opc

nombre = ""
opc = pintaMenú()
while(opc!=5):
    nombre= "Juan"
    opc=pintaMenú()

print(nombre)