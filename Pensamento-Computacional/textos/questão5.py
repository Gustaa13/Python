n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

if n1 < n2:
    n = n2
    n2 = n1
    n1 = n
if n1 < n3:
    n = n3
    n3 = n1
    n1 = n
if n2 < n3:
    n = n3
    n3 = n2
    n2 = n

if n1 == n2 == n3:
    print ('Todos são iguais a ' + str(n1))
elif n1 == n2:
    print ('Maiores: ' + str(n1))
    print ('Menor: ' + str(n3))
    print ('Não há elementos no meio')
elif n2 == n3:
    print ('Maior: ' + str(n1))
    print ('Menores: ' + str(n3))
    print ('Não há elementos no meio')    
else:
    print ('Maior: ' + str(n1))
    print ('Menor: ' + str(n3))
    print ('Meio: ' + str(n2))