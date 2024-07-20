def cargar(arreglo, arreglo2, arreglo3):
    while True:
        print("Ingrese el dato 1")
        dato=input()
        dato2=validar_positivo("ingrese la edad")
        dato3=validad_positivo("Entradas al cine")
        arreglo.append(dato)
        arreglo2.append(dato2)
        arreglo3.append(dato3)
        resp=input("Presione espacio para detener la carga")
        if resp==" ":
            break
def imprimir(arreglo1, arreglo2, arreglo3):
    print("Lista de datos")
    for i in range(len(arreglo1)):
        print(f"{arreglo1[i]} Edad:{arreglo2[i]} cantidad:{arreglo3[i]}")
    
def valida