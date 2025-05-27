import os
os.system('cls')
# CADENAS

import base64


a='bienvenidos'
#for i in range(len(a)):
x=a.find('v')
#print(x)
lista=list(a)




    


#print(a.find('i'))  #posicion

b='hola-mundo'.split('-')
#print(b)


#ejercicio 4

def verificar_email():
    email=input('ingrese mail:')
    cont=0
    for i in range (len(email)):
        if email[i]=='@':
            cont=cont+1
    if cont==1:
        print('correo correcto')
    else:
        print('Tiene más de un arroba o no tiene ninguno')    
#Principal
#verificar_email()

#ejercicio 5
frase='hola  python  mio'
fraseNueva = frase.replace("  ", " ")
#print(fraseNueva)

#ejercicio 6
def validar_cadena():
    cad=input('ingrese cadena:')
    if len(cad)>6:
      if not(cad.isdigit()) and not(cad.isalpha()) and not(cad.islower()):
          print('clave correcta')
      else:
          print('no cumple con los requisitos')
    else:
        print('error, la cadena debe ser mayor a 6 caracteres')    

#principal
#validar_cadena()

#ejercicio 11
def validar_dni():
    x=input('ìngrese dni:')
    while not(x.isdigit()) or len(x)!=8:
           x=input('ìngrese dni:')
    return x       

def buscar_repetido(dni,lista):
    for i in range(len(lista)):
        if lista[i]==dni:
            print('existe')
            break
        else:
            return dni
    
def clave():
    cad=input('ingrese clave:')
    if len(cad)>6:
      if not(cad.isdigit()) and not(cad.isalpha()) and not(cad.islower()):
          print('clave correcta')
      else:
          print('no cumple con los requisitos')
    else:
        print('error, la cadena debe ser mayor a 6 caracteres')  
    return cad 

def nombre():
    nom=input('ingrese nombre:')
    while len(nom)<3 or not(nom.isalpha()):
              nom=input('ingrese nombre:')
    return nom  

def buscar_area(area):
     cod=input('ingrese codigo area:')
     while not(cod in area):
         cod=input('ingrese codigo area:')   
     return cod    

def celular():
    area=['388','3887','3886','3888']
    cod=buscar_area(area)
    num=input('ingrese numero:')
    while len(num)!=7  or num[0]=='1' or num[1]==5:
        num=input('ingrese numero:')
    numero=cod+'-'+num
    return numero

def registrar():
    dni=validar_dni()
    if len(lista)!=0: 
       x=buscar_repetido(dni,lista)
    clav=clave()
    nom=nombre()
    num=celular()
    lista.append([dni,clav,nom,num])
    print(lista)

#principal
lista=[]
#registrar()


####modulo
def cambiar_vocal(cad,letra):
    x=cad.replace('e','E')
    return x
    

#Principal
cad='Roses are red violets are blue sugar is sweet and so are you'
letra='e'
a=cambiar_vocal(cad,letra)
print(a)






