quant_num = int(input('São quantos números? '))

lista, lista_num, parar = [], [], False

# Nesse trecho é pedido os dados, eles são separados e adcionados a outra lista como números inteiros
# E também são pegos os valores do primeiro e terceiro quartil e é calculado se a lista não é crescente
lista = input('Digite os dados: ')
for i in range(1, quant_num + 1):
    lista_num.append(int(lista.split()[i - 1])) 
    if i == round((quant_num + 1) * 1/4):
        primeiro_q = lista_num[i - 1]
    if i == round((quant_num + 1) * 3/4):
        terceiro_q = lista_num[i - 1]    
    if lista_num[i - 1] < lista_num[i - 2]:
        parar = True
        break

if parar:
    # Nesse trecho um erro é impresso se a lista não for crescente
    print ('Erro! Os números devem estar em ordem crescente!')
    breakpoint    
else:        
    # Nesse trecho é calculada a mediana
    if quant_num % 2 == 0:
        mediana = (lista_num[int((len(lista_num) / 2) - 1)] + lista_num[int(len(lista_num) / 2)]) / 2
    else:
        mediana = lista_num[len(lista_num) // 2]

    # Nesse trecho é calculado o limite inferior
    for c in range(quant_num):
        if lista_num[c] >= mediana - ((terceiro_q - primeiro_q) + 1.5): 
            limite_inf = lista_num[c]
            break

    # Nesse trecho é calculado o limite superior
    for c in range(quant_num):
        if lista_num[c] <= mediana + ((terceiro_q - primeiro_q) + 1.5):
            limite_sup = lista_num[c]

    # Nesse trecho são impressos todos os valores
    print ('Limtie inferior: ' + str(limite_inf))
    print ('1° quartil: ' + str(primeiro_q))
    print ('Mediana: ' + str(mediana))
    print ('3° quartil: ' + str(terceiro_q))
    print ('Limite superior: ' + str(limite_sup))