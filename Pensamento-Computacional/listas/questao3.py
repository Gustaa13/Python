quant_alunos = int(input('São quantos alunos? '))

lista_alunos_impares = []
lista_alunos_pares = []
print ('Digite os nomes dos alunos: ')
for posicao_aluno1 in range(1, quant_alunos + 1):
    nome = input('')
    if posicao_aluno1 % 2 == 0:
        lista_alunos_pares.append(nome)
    else:
        lista_alunos_impares.append(nome)
lista_alunos_pares.reverse()
print ('Nova lista: ')
for posicao_aluno2 in range(1, quant_alunos + 1):
    if posicao_aluno2 % 2 == 0:
        print (lista_alunos_pares[(posicao_aluno2 // 2) - 1])
    else: 
        print (lista_alunos_impares[posicao_aluno2 // 2])