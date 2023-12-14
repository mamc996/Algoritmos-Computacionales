
n=5 
for i in range(13):
    print(n, "X", i,"=", n*i)

#segunda forma#
for i in range(2 , 10 , 2):
    print(i)

#tercera forma#
for x in range(2):
    print("hola mundo")

#cuarta forma4#

for i in range(10):
    if i > 4:
        break
    print(i)


for i in range(10):
    if i > 4:
        print(i)
    if i==5:
        print("hola")    
        break
    print(i)


#quinta forma

for i in range(10):
    if i%2==0: 
        continue   

    print(i)