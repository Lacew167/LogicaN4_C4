def cargar(arreglo):
    while True:
        print("Ingrese el dato")
        dato=input
        arreglo.append(dato)
        resp=input("Presione espacio para cerrar el ciclo")
        if resp==" ":
            break

def menu_opciones():
    print("1) Registrar")
    print("2) Imprimir")
    print("3) Salir")
    print("Ingrese la opcion")
#mostrar
def mostrar(arreglo):
    for i in range(len(arreglo)):
        print(arreglo[i])


#cuerpo principal
nombres=[]
while True:
    menu_opciones()
    opcion=int(input())
    match opcion:
        case 1: cargar(nombres)
        case 2: print(mostrar)
        case 3: print()
        case _: print("Opcion errada")
    if opcion==3:
        break