qtd = int(input())
for i in range(qtd):
    n1, n2, n3 = list(map(float, input().split()))
    res = ((n1 * 2 + n2 * 3 + n3 * 5) / 10)
    print(round(res, 1))