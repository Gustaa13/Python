n = int(input('Digite um número: '))

for t in range(1, (int(n ** (1/3)) + 1)):
    if n % t == 0 and n % (t + 1) == 0 and n % (t + 2) == 0:
        print ('O número é triangular')
        break
    elif t == int(n ** (1/3)):
        print ('O número não é triangular')
        
