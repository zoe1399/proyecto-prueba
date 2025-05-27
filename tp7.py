import os
os.system('cls')

lista11=[]#lista vacia
lista1=['hola a todos', 'plasticola', 'tijera']  
lista2=['lapiz', 'goma',100,'regla'] #tamaño n=4 elementos, empiezan en 1 hasta 4
#'posicion u orden i: 0   , 1,   2 ,   3'

print(lista2[2]) # accedo al valor y muestro 100

lista2[1]='cartuchera' #modificando un valor de la lista
print(lista2)

#posiciones de una lista
for i in range (len(lista2)):
    print('posicion i')

# FORMAS DE RECORRER UNA LISTA
for i in range(len(lista2)):
    print('valor es:', lista2[i])
    print('posicion:',i)

for i, item in enumerate(lista2):
      print(i, item)      

suma=lista1+lista2
print(suma)
suma1=lista2+lista1
print(suma1)

lista2.append(lista1[1]) # agrego el ultimo valor
print(lista2)

n=len(lista1) # guarda el tamaño o cantidad de elementos que tiene la lista
print(n)
lista3=lista2
print(lista3)
lista3.append(lista1[n-1])
print(lista3)
# agregar al principio
lista3.insert(0,'iprg')
print(lista3)
lista3.insert(1,'PDI')
print(lista3)

n=len(lista3)//2
print(n)
lista3.insert(n,'xxxx')
print(lista3)

# EJERCICIO 2:
'''Escriba la función mayores_que(x, lista_valores) que cuente cuántos valores en la lista valores 
son mayores que x, por ejemplo mayores_que(5, [7, 3, 6, 0, 4, 5, 10]) devuelve el valor 3'''


def mayores_que(x,a):
    cont=0
    for i in range(len(a)):
        if x >a[i]:
            cont +=1
    return cont        

# principal
'''a=[7,3,6,0,4,5,10]
x=int(input('ingrese valor a buscar:'))
cont=mayores_que(x,a)
print('la cantidad de valores mayores a x son:', cont)'''

#ejercicio 4
'''Cargar una lista con N números enteros
● Mostrar los números ingresados y su posición
● Mostrar si los elementos de la lista se encuentran ordenados en forma descendente
● Mostrar los valores que superen el promedio de los valores ingresados
● Mostrar el mínimo de los valores ingresados y su posición
● Indicar qué elementos son valores primos 
● El algoritmo debe considerar que si no se cargó la lista previamente, no se 
pueda realizar alguna de las acciones solicitadas.'''

def cargar(a):
    N=int(input('tamaño de la lista:'))
    for i in range (N):
        valor=int(input('valor:'))
        a.append(valor)

def mostrar(a):
    #print(a)
    for i in range(len(a)):
        print(a[i], 'posicion:',i)

def ordenar_desc(a):
    a.sort() # ordena en forma ascendente
    print(a)

def promedio(a):
    suma=0
    for i in range(len(a)):
        suma +=a[i]
    prom=suma/len(a)
    return prom

def valores_mayor_promedio(a):
    prom=promedio(a)
    for i in range(len(a)):
        if a[i]>prom:
            print(a[i])

def minimo(a):
    min=a[0] # asigno el primer valor de la lista como minimo
    for i in range(1,len(a)):
        if a[i]< min:
            min=a[i]
            pos=i
    print('el minimo es:', min, 'está en la posicion:', pos)

#principal
a=[]
cargar(a)
print(a)
#mostrar(a)
#ordenar_desc(a)
#valores_mayor_promedio(a)
minimo(a)