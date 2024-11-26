def imprimePartes(lista, separador):
    lista_num = []
    comparador = []
    quant_separadores = lista.count(separador)

    print ('Sequências resultantes: ')
    for b in range(quant_separadores):
        posicao_separador = lista.index(separador)

        for a in range(posicao_separador):
            lista_num.append(lista[a])

        if lista_num != comparador:
            print(str(lista_num)[1:-1])

        for i in range(posicao_separador + 1):
            lista.pop(0)

        for c in range(len(lista_num)):
            lista_num.pop(0)

    if lista != comparador:
        print (str(lista)[1:-1])

quant_num = int(input('Serão quantos números? '))

sequencia = []
for i in range(quant_num):
    num = int(input())
    sequencia.append(num)

separador = int(input('Qual será o elemento separador? '))

imprimePartes(sequencia, separador)