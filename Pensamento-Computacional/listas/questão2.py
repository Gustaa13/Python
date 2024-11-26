quant_num = int(input('Qual a quantidade de números? '))

lista_num = []
print('Digite os valores: ')
for contador in range(0, quant_num):
    num = int(input(''))
    lista_num.append(num)
op = int(input('Qual a operação? '))
a = int(input('Qual o A? '))
b = int(input('Qual o B? '))
if op == 0:
    print ('{} + {} = {}'.format(lista_num[a - 1], lista_num[b - 1], lista_num[a - 1] + lista_num[b - 1]))
elif op == 1:
    print ('{} * {} = {}'.format(lista_num[a - 1], lista_num[b - 1], lista_num[a - 1] * lista_num[b - 1]))
else:
    print ('Operador inválido, os operadores são "0" para soma e "1" para multiplicação')