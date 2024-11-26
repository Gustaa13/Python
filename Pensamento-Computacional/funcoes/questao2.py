def funcaoPrincipal():
    opcao = 0
    saldo = 1000
    while True:
        opcao = exibeOpcoes(opcao)
        if opcao == 4:
            print ('Obrigado por usar os serviços do Caixa Eletrônico!')
            break
        else:
            saldo = processaOpcoes(opcao, saldo)

def funcaoSaldo(saldo):
    print ('Valor do saldo: ' + str(saldo))
    return saldo

def funcaoDeposito(saldo):
    deposito = float(input('Qual o valor do depósito: '))
    saldo = saldo + deposito
    funcaoSaldo(saldo)
    return saldo

def funcaoSaque(saldo):
    saque = float(input('Qual o valor do saque: '))
    saldo = saldo - saque
    if saldo < 0:
        print ('Saldo insuficiente!')
        saldo = saldo + saque
        return saldo
    else:
        funcaoSaldo(saldo)
        return saldo

def exibeOpcoes(x):
    print('Qual operacão você deseja realizar? ')
    print('1 - SAQUE')
    print('2 - DEPóSITO')
    print('3 - SALDO')
    print('4 - SAIR')
    x = int(input('Escolha: '))
    return x

def processaOpcoes(opcao, saldo):
    if opcao == 1:
        saldo = funcaoSaque(saldo)
        return saldo
    elif opcao == 2:
        saldo = funcaoDeposito(saldo)
        return saldo
    elif opcao == 3:
       saldo = funcaoSaldo(saldo)
       return saldo
    else:
        print ('Opcão inválida, tente novamente!')

funcaoPrincipal()