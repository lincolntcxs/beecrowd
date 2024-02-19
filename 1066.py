posi = 0
nega = 0
par = 0
imp = 0

for i in range(5):
    num = int(input())
    if(num > 0):
        posi += 1
    if(num < 0): 
        nega += 1
    if(num % 2 != 0):
        imp += 1
    else:
        par += 1
print(str(par) + " valor(es) par(es)")
print(str(imp) + " valor(es) impar(es)")
print(str(posi) + " valor(es) positivo(s)")
print(str(nega) + " valor(es) negativo(s)")