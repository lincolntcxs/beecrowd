qtd = int(input())
for i in range(qtd):
    x, y = list(map(float, input().split()))
    if(y == 0):
        print("divisao impossivel")
    else:
        print(str(x / y))