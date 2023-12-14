paga=float(input("ingrese paga: "))
horas=float(input("ingrese horas trabajadas: "))

salario=(paga * horas)

if horas>=0 and horas<=40:
    print("sueldo dentro de las horas: " + str(salario))

if horas>=40:
    salario2= (paga * horas) * 0.5
    print("sueldo + sueldo extra: " + str(salario2))

else :
    horas<=0 or paga<=0
    print("el monto de sueldo y las paga estan mal ingresadas")