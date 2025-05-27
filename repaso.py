
def validar_legajo(m_empleados,legajo_nuv):
    band=True
    for i in range(len(m_empleados)):
        if legajo_nuv==m_empleados[i][0]:
            band=False
    if band==True:
        print("no hay ningun legajo parecido a este")
    return band
def validar_legajo2(m_empleados,legajo_nuv):
    for i in range(len(m_empleados)):
        if legajo_nuv==m_empleados[i][0]:
            return True
    print("no hay ningun legajo parecido a este")
    return False


def agregar(m_empleados):
    nuevoempleado=[]
    antiguedad=int(input("ingrese sus años de antiguedad: "))
    factor=float(input("ingrese su factor: "))
    while True:
        legajo_nuv=str(input("ingrese nuevo legajo: "))
        bandera=validar_legajo(m_empleados,legajo_nuv)
        if bandera==True:
            nuevoempleado.append([legajo_nuv,antiguedad,factor])
            m_empleados.append(nuevoempleado)
            break
        else:
            print("error legajo ya existe")

def buscar(lista,x):
    for i in range(len(lista)):
        if x==lista[i][0]:
            return i
    return -1     

#buscar(m_empleados,legajo,0)
#buscar(m_empleados,legajo,0)


def buscarlegajo(m_empleados,buscarlegajo,dis):
    bandera2=False
    for i in range (len(m_empleados)):
        if m_empleados[i][0]==buscarlegajo:
            bandera2=True

    if bandera2==True:
        m_empleados[i][2]-=dis
        print('exitoso')
        return m_empleados

def disminuir(m_empleados):
    legajo=str(input("ingrese su legajo: "))
    for i in range(len(m_empleados)):
        if m_empleados[i][0]==legajo:
            dis=float(input("cantidad que desee disminuir del factor: "))
            m_empleados[i][2]-=dis
            return 
    print("no se encontro el legajo")
  
def disminuir(m_empleados):
    legajo=str(input("ingrese su legajo: "))
    pos=buscar(m_empleados,legajo)
    if pos!=-1:
        dis=float(input("cantidad que desee disminuir del factor: "))
        m_empleados[pos][2]-=dis
    else:
        print("no se encontro el empleado a disminuir")


def calcular(m_empleados):
    multiplicar=0
    for i in range(len(m_empleados)):
        multiplicar+=m_empleados[i][1]*m_empleados[i][2]
    print(multiplicar)

#principal
m_empleados=[["321iv",8,23],["234zo",9,99.33]]
#agregar(m_empleados)
print(m_empleados)
disminuir(m_empleados)
print(m_empleados)
#calcular(m_empleados)

def cambiar_vocal(cad,letra):
    x=cad.replace('e','E')
    return x
    

#Principal
cad='Roses are red violets are blue sugar is sweet and so are you'
letra='e'
a=cambiar_vocal(cad,letra)
print(a)