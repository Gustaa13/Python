n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

for n in range(n1, n2 + 1):
    print ('=-=-=-= Tabuada de {} =-=-=-='.format(n))
    for t in range(1, 11):
        print('{} x {} = {}'.format(n, t, n * t))
