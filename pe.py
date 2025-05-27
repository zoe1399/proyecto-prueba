a= float(input("ingrese artista lateral: "))
h=float(input("ingrese altura: "))
l=float(input("ingrese lado base: "))
if (a>0) and (h>0) and (l>0):
    total=l*(l+(4*h*2+l*2)**(1/2))
    sub=(l*2*h)/3
    print("la superficie es ", total)
    print("el volumen es", sub )
else:
    print("escribir numero positivoo")
