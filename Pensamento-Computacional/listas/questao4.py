quant_jog = int(input('Quantidade de jogadores? '))

lista, lista_tudo, tent_s, tent_b, tent_a, s, b, a = [], [], [], [], [], [], [], []

print ('Digite os dados para cada jogador: ')
for i in range(quant_jog):
    lista = input('')
    lista_tudo.extend(lista.split())

tent_s, tent_b, tent_a, s, b, a 
for c in range(quant_jog):
    tent_s.append(int(lista_tudo[1 + 7 * c]))
    tent_b.append(int(lista_tudo[2 + 7 * c]))
    tent_a.append(int(lista_tudo[3 + 7 * c]))
    s.append(int(lista_tudo[4 + 7 * c]))
    b.append(int(lista_tudo[5 + 7 * c]))
    a.append(int(lista_tudo[6 + 7 * c]))

print ('As estatísticas do jogo são as seguintes: ')
print ('Pontos de Saque: {}%'.format(round(((sum(s) / sum(tent_s)) * 100), 2)))
print ('Pontos Bloqueio: {}%'.format(round(((sum(b) / sum(tent_b)) * 100), 2)))
print ('Pontos de Ataque: {}%'.format(round(((sum(a) / sum(tent_a)) * 100), 2)))