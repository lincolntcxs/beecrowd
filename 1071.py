x = int(input())
y = int(input())
total = 0

for i in range(y + 1 , x):
    if(i % 2 != 0):
        total += i    
print(total)