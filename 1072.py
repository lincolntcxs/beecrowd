qtd = int(input())
dento = 0
fora = 0
for i in range(qtd):
    num = int(input())
    if(num < 10 or num > 20):
        fora += 1
    else:
        dento += 1
print(str(dento) + " in")
print(str(fora) + " out")