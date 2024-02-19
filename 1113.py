while(1):    
    try:   
        x, y = list(map(int, input().split()))
        if(x == y):
            break
        if(x > y):
            print("Decrescente")
        else:
            print("Crescente")
    except EOFError:
        break