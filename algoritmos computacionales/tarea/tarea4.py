precio=float(input("ingrese el precio del articulo: "))

if precio>=500:
    descuento= precio * 0.30
    precio1= precio - descuento
    print("descuento del 30% : " + str(precio1))

if precio<500 and precio>=200:
    descuento2= precio * 0.20 
    precio2= precio - descuento2
    print("el descuento del 20%: " + str(precio2))

if precio<200 and precio>=100:
    descuento3= precio * 0.10
    precio3 = precio - descuento3
    print("el descuento del 10%: "+ str(precio3))

else:
    precio<100
    print("no aplica descuento: " + str(precio))