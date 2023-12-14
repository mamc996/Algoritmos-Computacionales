#tabla de multiplicar del 1 al 12  
# \n = es para dar un salto de linea -- alt + 92 -- #

for n in range (1 , 13):
    print("Tabla del", n)
    
    for i in range (13):
        print(n,"X",i , "=", n*i)


#ingrese un numero y listar los pares hasta el numero ingresado#

n=int(input("ingrese: "))
for i in range(2, n+1, 2):
    print(i)

#ingresar un numero y verificar si es primo#

n=int(input("ingrese: "))
cont=1
for i in range(1, n+1):
    if n%i==0: 
        cont=cont+1
if cont==2:
    print("el numero", n, "si es primo")

else:
    print("el numero", n,"no es primo")


#el numero ingresado debe de ser perfecto#
n=int(input("ingrese: "))
sd=0
for i in range(1, n+1):
    if n%i==0: 
        sd=sd+1
if sd==n:
    print("el numero", n, "SI es un numero perfecto")

else:
    print("el numero", n,"NO es un numero perfecto")
