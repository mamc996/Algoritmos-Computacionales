lado1=float(input("ingrese la primera longitud: "))
lado2=float(input("ingrese la segunda longitud: "))
lado3=float(input("ingrese la tercera longitud: "))

if lado1>lado2 and lado1>lado3:
    mayor=lado1

elif lado2>lado1 and lado2>lado3:
    mayor=lado2

else:
    mayor=lado3

suma = lado1 + lado2 + lado3 - mayor

if mayor<suma:
    if lado1==lado2 and lado2 == lado3:
        tipo="Equilatero"
    elif lado1==lado2 or lado1==lado3 or lado2 == lado3:
        tipo="Isoseles"
    else:
        tipo="Escaleno"

else:
    tipo="No es un triangulo"
print(tipo)