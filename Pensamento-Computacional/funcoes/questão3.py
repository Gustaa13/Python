def primos(x):
    y = []
    b = []
    b = x
    b.sort()
    for n in range(1, (b[-1]) + 1):
        div = False
        for d in range(2, int(n ** (1/2)) + 1):
            if n % d == 0:
                div = True
                break
        if not div and n != 1:
            y.append(n)        
    for a in range(len(b)):
        if b[a] in y:
            print('{} é primo'.format(b[a]))
        else:
            lista_num_nova.append(b[a])

def divisores(z):
    w = []
    for i in range(len(z)):
        for b in range(1, z[i] + 1):
            if z[i] % b == 0:
                w.append(b)
        print ('{} não é primo, os divisores são: {}'.format(z[i], str(w)[1:-1]))
        w.clear()

quant_num = int(input('São quantos números? '))

lista_num = []
lista_num_nova = []
for i in range(quant_num):
    num = int(input())
    lista_num.append(num)

print ('A classificação é: ')
primos(lista_num)
divisores(lista_num_nova)