t = input('Texto: ')
i1 = int(input('i1: '))
i2 = int(input('i2: '))

if i1 > i2:
    i = i1
    i1 = i2
    i2 = i

if i2 >= len(t):
    print ('Erro! Os índices precisam ser menores do que o tamanho do texto ({}).'.format(len(t)))
else:
    print ('Parte 1: ' + t[:i1])
    print ('Parte 1: ' + t[:i2])
    print ('Parte 3: ' + t[i1:i2])
    print ('Parte 4: ' + t[i1:])
    print ('Parte 5: ' + t[i2:])