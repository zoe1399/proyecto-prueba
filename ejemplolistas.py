def cargarlista():
    lista=[]
    longitud=int(input("ingrese la cantidad de numeros a cargar:"))
    for i in range(longitud):
        numero=int(input("ingrese el numero"))
        lista.append(numero)
    return lista

def mostrarposicion(lista):
    for i in range (len(lista)):
        print(i,lista[i])#esto muestra la posicion (i) y el valor en esa poscion(lista(i))

def mostrardescendente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:  # Si algún elemento es menor que el siguiente
            print("esta ordenada en forma descendete")

def mostrarpromedio(lista):
    promedio=sum(lista)/len(lista)
    print("promedio",promedio)
    for i in range(len(lista)):
        if lista[i] >promedio:
            print(lista[i])

def mostrarminimo(lista):
    for i in range(len(lista) - 1):
        if lista[i] < lista[i + 1]:  # Si algún elemento es menor que el siguiente
            print("minimo valor:",lista[i])


#principal
lista=cargarlista() 
longitud=len(lista)
print(longitud)
mostrarposicion(lista)
mostrardescendente(lista)
mostrarpromedio(lista)
mostrarminimo(lista)
print(lista)
