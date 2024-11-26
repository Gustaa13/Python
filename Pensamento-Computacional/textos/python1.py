import math 

s = input('Você quer fazer uma operação? [s/n]')
while s == ('s'):
    a = float(input('Qual o primeiro número: '))
    op = input('Qual o operador? ')
    b = float(input('Qual o segundo número: '))

    if op == ('+'):
        print (a + b)
    elif op == ('-'):
        print (a - b)
    elif op == ("*"):
        print (a * b)
    elif op == ('/'):
        print (a / b)
    else:
        print ("Operador não existente")
        
    s = input('Você quer fazer uma operação? [s/n]')

