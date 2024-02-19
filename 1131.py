a = 0
total = 0
vitGrem = 0
vitInt = 0
empates = 0

while(a != 2):
    inter, gremio = list(map(int, input().split()))
    total += 1
    if(inter > gremio):
        vitInt += 1
    elif(inter < gremio):
        vitGrem += 1
    else:
        empates += 1
    print("Novo grenal (1-sim 2-nao)")
    a = int(input())
    if(a == 2):
        print( str(total) + " grenais")
        print("Inter:" + str(vitInt))
        print("Gremio:" + str(vitGrem))
        print("Empates:" + str(empates))
        if(vitInt > vitGrem):
            print("Inter venceu mais")
        elif(vitInt < vitGrem):
            print("Gremio venceu mais")
        else:
            print("Nao houve vencedor")