a = 0
alco = 0
gaso = 0
dies = 0

while(a != 4):
    a = int(input())
    if(a == 1):
        alco += 1
    elif(a == 2):
        gaso += 1
    elif(a == 3):
        dies += 1
    if(a == 4):
        print("MUITO OBRIGADO")
        print ("Alcool: " + str(alco))
        print ("Gasolina: " + str(gaso))
        print ("Diesel: " + str(dies))