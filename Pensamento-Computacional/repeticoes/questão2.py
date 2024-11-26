n = int(input('Você quer quantos termos da sequência de fibonnaci? '))

f3 = 1
f2 = 0

l = []

for c in range(1, n + 1):
    l.append(f3) 
    f1 = f2
    f2 = f3
    f3 = f2 + f1

print('Os {} primerios termos da sequência de fibonnaci são: '.format(n) + str(l)[1:-1])
