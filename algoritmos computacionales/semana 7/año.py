d=int(input('Ingresar dia:'))
m=int(input('Ingresar mes:'))
a=int(input('Ingresar año:'))
if a%4==0:
    nd=29
else:
    nd=28
 
if (d>=23 and d<=31 and m==12)or(d>=1 and d<=31 and m==1)or(d>=1 and d<=nd and m==2)or(d>=1 and d<=22 and m==3):
    print('La estación es verano')
else:
    print('La fecha ingresada no corresponde a verano')