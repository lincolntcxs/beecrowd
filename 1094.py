casos = int(input())
total = 0
coelhos = 0
ratos  = 0
sapos = 0

for i in range(casos):
    qtd, tipo = input().split()
    qtd = int(qtd)
    if(tipo == 'C'):
        coelhos += qtd
    elif(tipo == 'R'):
        ratos += qtd
    elif(tipo == 'S'):
        sapos += qtd
    total += qtd

print("Total: " + str(total) + " cobaias")
print("Total de coelhos: " + str(coelhos))
print("Total de ratos: " + str(ratos))
print("Total de sapos: " + str(sapos))

perco = float(coelhos / total) * 100
perra = float(ratos / total) * 100
persa = float(sapos / total) * 100
print("Percentual de coelhos: " + "{:.2f}".format(perco) + " %")
print("Percentual de ratos: " + "{:.2f}".format(perra) + " %")
print("Percentual de sapos: " + "{:.2f}".format(persa) + " %")