x, y = list(map(int, input().split())) 

while x > 0 or y > 0:
    soma = 0
    maior = 0
    menor = 0
    if(x > y):
        maior = x
        menor = y
    else:
        maior = y
        menor = x
    for i in range(menor, maior + 1):
        print(i, end =" ")
        soma += i
    print("Sum=" + str(soma))
    x, y = list(map(int, input().split())) 