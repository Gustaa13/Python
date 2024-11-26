def leitura():
    notas = [0, 0]
    for i in range(2):
        notas[i] = float(input("Digite a nota do aluno: "))
    return notas

def media(notas):
    media = (notas[0] + notas[1])/2
    print("Média: %f" %media)

    if(media >= 7.0):
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")

    return

notas = [0, 0]
notas = leitura()
media(notas)
