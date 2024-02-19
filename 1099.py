qtd = int(input())
for i in range(qtd):
    x, y = list(map(int, input().split()))
    if(x > y):
        maior = x
        menor = y
    else:
        maior = y
        menor = x
    
    soma = 0
    for j in range(menor + 1, maior):
        if(j % 2 != 0):
            soma += j
    print(soma)
    