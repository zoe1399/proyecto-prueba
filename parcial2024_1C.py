def buscar(lej,m_empleado):
    existe=0
    pos=-1
    for i in range(len(m_empleado)):
        if m_empleado[i][0]==lej:
            existe=1
            pos=i
    return existe,pos        

def agregar(m_empleado):
    legajo=input('ingrese legajo:')
    antiguedad=int(input('antiuedad:'))
    factor=float(input('factor:'))
    
    x=buscar(legajo,m_empleado)
    #agregar
    if x==0:
        m_empleado.append([legajo,antiguedad,factor])
    else:
        print('ya existe el empleado')  

def disminuir(m_empleado):
    legajo=input('legajo:')
    x,pos=buscar(legajo,m_empleado)
    if x==1:
        fact=float(input('ingrese factor:'))
        m_empleado[pos][2] -=fact
    else:
        print('no existe empleado')


#principal
m_empleado=[['100',5,2.5],['250',10,7]]
#agregar(m_empleado)
#print(m_empleado)
disminuir(m_empleado)
print(m_empleado)
