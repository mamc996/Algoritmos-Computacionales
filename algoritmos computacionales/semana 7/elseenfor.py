#permite que el programa siga continuando

for i in range(10):
    if i % 2 ==0:
        continue
    print(i)

else:
    print("programa terminado")

#corta el proceso del programa 

for i in range(10):
    if i > 4:
        break
    print(i)
else:
    print("no se ejecutará el programa")    



n=int(input("ingrese el numero: ")) 
for i in range(13):
    print(n, "X", i,"=", n*i)