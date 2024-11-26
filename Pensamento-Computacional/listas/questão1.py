num_nomes = int(input('Quantos alunos? '))

lista_nomes = []
for contador in range(0, num_nomes):
    nomes = input('')
    lista_nomes.append(nomes)
lista_nomes.reverse()   
print ('Você degitou: ')
for posicao in range(0, num_nomes):
    print (lista_nomes[posicao])
