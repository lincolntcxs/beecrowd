leuduas = 0
media = 0
while(leuduas != 2):
    nota = float(input())
    if(nota < 0 or nota > 10):
        print("nota invalida")
    else:
        media += nota
        leuduas += 1
print("media = " + "{:.2f}".format(media/2))