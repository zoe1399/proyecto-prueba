def validar(codigo,nuevo_codigo):
    for i in range(len(codigo)):
        if nuevo_codigo!=codigo[i]:
            print("este codigo es distinto a los demas")
            return nuevo_codigo
        print("este codigo ya existe")

def agregar(codigo):
    stock_nuevo=int(input("ingrese su stock: "))
    precio_nuevo=float(input("ingrese su precio: "))
    while True:
            nuevo_codigo=str(input("ingrese el codigo del nuevo articulo: "))
            bandera=validar(codigo,nuevo_codigo)
            if bandera==nuevo_codigo:
                codigo.append(nuevo_codigo)
                stocks.append(stock_nuevo)
                precio.append(precio_nuevo)
                break      
            print("error de codigo")


def aumentar(stocks):
    cod=str(input("ingrese el codigo del articulo: "))
    for i in range(len(codigo)):
        if codigo[i]==cod:
            cant=int(input("cantidad que desee aumentar: "))
            stocks[i]+=cant
            return 
    print("no se encontro el codigo")   
    """ggggg""     
              
         
            


codigo=["12q","31we","13re"]
stocks=[3,5,8]
precio=[2.14,4.21,5.67]
agregar(codigo)
print(codigo)
aumentar(stocks)
print(stocks)"""