sueldo=float(input("ingrese el sueldo: "))

if  sueldo>=0 and sueldo<=999:
     residuo= sueldo * 0.1
     sueldo1= sueldo - residuo
     print("sueldo menor a 1000, tu sueldo es: " + str(sueldo1))

if sueldo>=1000 and sueldo<=1999:
    residuo2 = sueldo * 0.05
    sueldo2 = sueldo - residuo2
    print("sueldo menor a 2000, tu sueldo es: " + str(sueldo2))

if sueldo>=2000:
    residuo3=sueldo * 0.03
    sueldo3= sueldo - residuo3 
    print("sueldo mayor a 2000, tu sueldo es: " + str(sueldo3))

else: 
    sueldo<=0
    print("error al ingresar sueldo")






