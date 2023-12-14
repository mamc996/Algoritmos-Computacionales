n1= float(input("primera nota: "))
n2= float(input("segunda nota: "))
promedio= (n1 + n2) / 2

if promedio >= 13 and promedio <= 20:

    print("el alumno esta aprobado ")
    print("el promedio del alumno es: "+ str(promedio))

if promedio >=0 and promedio<13:
    print("el alumno esta desaprobado")
    print("el promedio del alumno:"+ str(promedio))

else:
    print("error: por favor revisar las notas ingresadas")    


