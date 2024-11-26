n1 = int(input('n1: '))
n2 = int(input('n2: '))

if n1 > n2:
    n = n2
    n2 = n1
    n1 = n

l = []
p = [2, 3]

for i in range(n1, n2):   
    for p1 in range(2, int(i ** (1/2) + 2)):   
        div = True
        div2 = False
        for c in p:
            if p1 % c == 0:
                div = False
                break
        if (i % c == 0 or i % 3 == 0) and i != 3 and i % 2 != 0:
            div2 = True
            break
    if div:
        p.append(p1)  
    if div2:
        l.append(i) 

print('números ímpares não primos entre [{}, {}]: '.format(n1, n2) + str(l)[1:-1])