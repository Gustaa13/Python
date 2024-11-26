n1 = int(input('Digite o primeiro núemro: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    n = n2
    n2 = n1
    n1 = n
    
p = []
for n in range(n1, n2 + 1):
    div = False
    for d in range(2, int(n ** (1/2)) + 1):
        if n % d == 0:
            div = True
            break
    if not div and n != 1:
        p.append(n)
print ('Existem {} números primos entre {} e {}.'.format(len(p), n1, n2))
print ('Os primos são: ' + str(p)[1: -1])