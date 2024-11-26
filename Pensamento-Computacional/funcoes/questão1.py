lista1, lista2, lista3, lista4, lista_encripitada = ["a", "b", "c", "d", "e", 'A', 'B', 'C', 'D', 'E'], ['f', 'g', 'h', 'i', 'j', 'F', 'G', 'H', 'I', 'J'], ['k', 'l', 'm', 'n', 'o', 'K', 'L', 'M', 'N', 'O'], ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], []

def fun_nome(x):
    for i in range(len(x)):
        if x[i] in lista1:
            lista_encripitada.append(1)
        elif x[i] in lista2:
            lista_encripitada.append(2)
        elif x[i] in lista3:
            lista_encripitada.append(3)
        elif x[i] in lista4:
            lista_encripitada.append(4)
        else:
            lista_encripitada.append(5)
    cripto = ''.join(str(elemento) for elemento in lista_encripitada)
    print ('Encriptado: ' + cripto)

nome = input('Digite o texto: ')
fun_nome(nome)