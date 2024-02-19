a = 0
j = 0
const = 1
for i in range(11):
    for c in range(3):
        print("I=" + str(round(a, 1)) + " J=" + str(round((const+ j), 1)) )
        # print("I=" + "{:.1f}".format(a) + " J=" + "{:.1f}".format(const + j))
        const += 1
    a += 0.2
    j += 0.2  
    const = 1