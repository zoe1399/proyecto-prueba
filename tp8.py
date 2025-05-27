import random
#listas simples
a=['Maria', 100, 'a']  #tamaño 3
#  i=0       i=1   i=2  i es posicion

#listas paralelas
A=['Noelia', 'Pedro', 'Juan'] # nombres alumnos
B=[4256, 8596,6321] # legajo alumnos

for i in range(len(A)):
    if  A[i]  =='Pedro':
        print(B[i])

# listas dobles o lista de lista
c=[['perez',85],['Casasola',10],['Salto',100]]  # tengo 3 listas simples
#     j=0   j=1    j=0      j=1     j=0   j=1
#      i=0            i=1            i=2
print(c[1][1]) #muestra 10
print(c[2][1])

# ejercicio 6: listas paralelas
def validar_n():
    n=int(input('cantidad a cargar:'))
    while n<5 or n>50:
        n=int(input('ingrese un valor entre 10 y 50:'))
    return n    
def validar_peces():
    c=int(input('cantidad peces:'))
    while c<0:
        c=int(input('cantidad peces:'))
    return c    

def cargar(a,b):
    x=validar_n()
    for i in range(x):
        nom=input('nombre:')
        cant=validar_peces()
        a.append(nom)
        b.append(cant)
   
def promedio(b):
    suma=0
    for i in range(len(b)):
        suma=suma+b[i]
    prom=suma/len(b)
    print(prom)
    return prom

def mostrar_participante(posi,a):
    for i in range(len(posi)):
        x=posi[i]
        print(a[x])

def mayor(b,alumnos):            #[10,15,3,15,15]
   max=-1
   posi=[]
   for i in range(len(b)):
       if b[i]>max:
           c=0
           max=b[i]      
           po=i
           c=c+1
       elif b[i]==max and c>=1:
           c=c+1
           pos=i
           posi.append(pos)
   posi.append(po)    
   print(posi)
   mostrar_participante(posi,a)
      
def disminuir(b):
    pos=int(input('posicion:'))  
    x=int(input('cantidad a restar:'))    
    b[pos]=b[pos]-x        
    print(b)
 

#principal
'''a=[]
b=[]
cargar(a,b)
print(b)
#p=promedio(b)
mayor(b,a)
disminuir(b)'''

# matrices
def cargar(a):
    N=6
    for i in range(N):
        fil=[]
        for j in range(N):
            fil.append(random.randint(1,10))
        a.append(fil)        
        
def recorrido1(a):
    for col in range(len(a)):
        for fil in range(len(a)):
            print(a[fil][col])

def recorrido2(a):
    for fil in range(len(a)):
        for col in range(len(a)):
            print(a[fil][col])

def recorrido3(a):
    N=len(a)//2
    x=len(a)
    i=0
    # recorrido L invertida
    for col in range(N-1,-1,-1):
        for fil in range(x-1,i-1,-1):
            print(a[fil][col])
        #recorrido izquierda
        for col2 in range(col-1,-1,-1):   
            print(a[fil][col2])
        i +=1
    # recorrido en L
    
#principal
a=[[7, 3, 7, 6, 2, 4],
   [3, 3, 2, 1, 4, 3],
   [9, 6, 1, 5, 2, 1],
   [5, 5, 8, 9, 4, 1],
   [1, 4, 8, 8, 3, 2], 
   [1, 3, 3, 6, 4, 2]]

#cargar(a)
print(a)
#recorrido1(a)
#recorrido2(a)
recorrido3(a)

