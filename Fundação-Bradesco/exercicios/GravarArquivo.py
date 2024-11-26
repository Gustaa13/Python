caminho_arquivo = 'Textos/arqText.txt'

arquivo = open(caminho_arquivo, 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Prática')
arquivo.close()

leitura = open(caminho_arquivo, 'r')
print(leitura.read())
leitura.close()