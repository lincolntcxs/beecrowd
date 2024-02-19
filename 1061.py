dia, dataini = input().split()
dataini = int(dataini)
hini, mini, sini = map(int, input().split(":"))

dia, datafin = input().split()
datafin = int(datafin)
hfin, mfin, sfin = map(int, input().split(":"))

data = datafin - dataini
hora = hfin -  hini
min = mfin - mini
seg = sfin - sini

if(seg < 0):
    seg += 60
    min -= 1
if(min < 0):
    min += 60
    hora -= 1
if(hora < 0):
    hora += 24
    data -= 1
    
print(str(data) + " dia (s)")
print(str(hora) + " hora (s)")
print(str(min) + " minuto (s)")
print(str(seg) + " segundo (s)")