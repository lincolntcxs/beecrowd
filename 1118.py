a = 0
media = 0
loop = 0

while(a != 2):
    a = float(input())
    if(a >= 0 and a <= 10):
        media += a
        loop += 1
    else:
        print("nota invalida")
    if(loop == 2):
        print("media = {:.2f}".format(media / 2))
        print("novo calculo (1-sim 2-nao)")
        a = int(input())
        loop = 0
        media = 0
        while(a > 2 or a < 1):
            print("novo calculo (1-sim 2-nao)")
            a = int(input())