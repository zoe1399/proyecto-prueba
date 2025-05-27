# DICCIONARIOS

a={} # vacio

a={1:'Maria',2:'Juan'}
b={1:['maria',18,6], 2:['juan',25,2]}

#agregar un elemento
a[3]='Pepito'
print(a)

#recorrido
for clave, valor in a.items():
    print(clave,valor)

def buscar(x,agenda):
    existe=agenda.get(x,0)
    return existe

#principal
'''x=int(input('clave:'))
valor=buscar(x)
if valor==0:
    print('no existe')
else:
    print(valor)    '''


#ejercicio 2
def agregar(agenda):  
    nombre=input('nombre:')
    existe=buscar(nombre,agenda)
    if existe!=0:
        print(existe)
        resp=input('desea modifica el telefono:(s/n):')
        if resp=='s':
            tel=int(input('ingrese telefono:'))
    else:
        telefono=int(input('ingrese telefono a agregar:'))
        agenda[nombre]=telefono       

def buscar2(agenda):
    cadena=input('ingrese cadena a buscar:')
    for clave, valor in agenda.items():
         nombre=clave
         b=nombre.startswith(cadena)
         if b:
             print(valor)

def borrar(agenda):
    nom=input('nombre a borrar:')
    existe=buscar(nom,agenda)
    if existe==0:
        print('no existe contacto a borrar')
    else:
        resp=input('Desea borrar el contacto (s/n):')    
        if resp=='s':
            t=agenda.pop(nom)

def listar(agenda):
    for clave, valor in agenda.items():
        print(clave, valor)
   

#principal
'''agenda={'maria':5839676,'Juan':4758691,'marimar':4589623}
print(agenda)
agregar(agenda)
buscar2(agenda)
borrar(agenda)
listar(agenda)'''

#listas
def buscar_materia(cod,materia):
    pos=-1
    for i in range(len(materia)):
        if materia[i][0]==cod:
            pos=i
    return pos

def agregar_alumno(B,A):
    cod=int(input('codigo materia:'))
    pos=buscar_materia(cod,A)
    if pos==-1:
        print('no existe la materia')
    elif A[pos][5]<A[pos][4]:
        dni=int(input('dni:'))    
        nomb=input('nombre:')
        B.append([cod,dni,nomb])
        A[pos][5]+=1


def importe(A,B):
    cod=int(input('codigo:'))
    pos=buscar_materia(cod,A)
    if pos!=-1:
        total=A[pos][3]*A[pos][5]
        print(total)
    else:
        print('no existe materia')

def promedio(A):
    suma=0
    for i in range (len(A)):
        suma +=A[i][3]
    prom=suma/len(A)    
    return prom

def cargar_C(A):
    p=promedio(A)
    for i in range(len(A)):
        if A[i][3]<p:
            C.append(A[i])

#principal
A=[[100,'algebra',1,200,100,30],  #[codigo, desc,año,precio,cupo,inscriptos]
        [200,'iprog1',1,350,500,480]]
B=[]
C=[]
#agregar_alumno(B,A)
print(B)
print(A)
#importe(A,B)
cargar_C(A)
print(C)