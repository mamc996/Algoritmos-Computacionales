articulo= float(input("ingrese el precio del articulo: "))

iva= articulo * 0.15

preciobruto= articulo + iva

if preciobruto<50.00:
    print( "el precio es: " + str(preciobruto) + " pesos")

if preciobruto>=50.00:
    descuento= preciobruto * 0.05
    precio2= preciobruto - descuento
    print("el precio con descuento es: " + str(precio2) + " pesos")

else:
    articulo<=0
    print("el precio esta equivocado")