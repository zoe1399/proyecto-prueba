# RECURSIVIDAD
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1) 


# PRINCIPAL
'''n=int(input('numero:'))
fact=factorial(n)
print('el resultado es:',fact)'''

materias=[['AM',2024,600,300],
          ['ìprog1',2024,600,150],
          ['algebra', 2024,300,10]]

corredores=['J','M','T']
km=[10,20,5]
tiempo=[30,15,45]

'''min=9999
for i in range(len(tiempo)):
    if tiempo[i]<min:
          min=tiempo[i]
          pos=i

print(corredores[pos])'''


min=9999
for i, item in enumerate(tiempo):
       if item<min:
            min=item
            pos=i
print(corredores[pos])

#lista=[codigo,descripcion,stock]

def buscar(cod, lista):
     band=-1
     for i in range(len(lista)):
          if lista[i]==cod:
               band=0
               pos=i
     return band,pos

def agregar(lista):
     cod=int(input('codigo:'))
     x,pos=buscar(cod,lista)
     desc=input('desc:')
     if x==-1:
          lista.append([cod,desc])
     else:
          print('existe')     

def eliminar(lista):
     cod=int(input('ingrese codigo a eliminar:'))
     x,pos=buscar(cod,lista)
     if x==-1:
          print('No existe el codigo a eliminar')
     else:
          del lista[pos]     

def modificar(lista):
     for i in range(len(lista)):
          lista[i][2]=lista[i][2]-10



cad='Roses are red violets are blue sugar is sweet and so are you'
letra='e'

def cambiarVocal(cad,letra):
    nuevo= cad.replace(letra,letra.upper())
    print(nuevo)

def contarPalabras(cad):
     frase=cad.split(' ')
     print(len(frase))

def contarVocalRepetida(cad):
     print(cad.count('e'))
     

def mostrarPalabraMas3Caracteres(frase):
    fra=frase.split(' ')
    print(fra)
    nuevo=[]
    for i in range(len(fra)):
         long=len(fra[i])
         if long>3:
            nuevo.append(fra[i])
    print(nuevo)      

def eliminar(nombres,legajos,notas):
    legajo = int(input('Ingrese el legajo: '))
    for pos, elem in enumerate(nombres):
        if legajo == elem:
            del nombres[pos]
            del legajos [pos]
            del notas [pos]
    else:
        print('nose encontro el legajo')
    return nombres,legajos,notas    





#principal
frase='El rey Pele era un futbolista fantástico'
#cambiarVocal(cad,letra)   
#contarPalabras(cad) 
#contarVocalRepetida(cad)
mostrarPalabraMas3Caracteres(frase)