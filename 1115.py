while(True):
    try:
        x, y = list(map(int, input().split()))
        if(x == 0 or y == 0):
            break
        if(x > 0 and y > 0):
            print("primeiro")
        elif(x > 0 and y < 0):
            print("quarto")
        elif(x < 0 and y > 0):
            print("segundo")
        else: print("terceiro")
    except EOFError:
        break