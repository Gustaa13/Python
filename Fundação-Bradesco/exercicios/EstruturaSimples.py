a = int(input("Informe um valor para a variável A: "))
b = int(input("Informe um valor para a variável B: "))

if(a > b):
    aux = a
    a = b
    b =  aux
elif(a < b):
    print()
    
print("O valor da variável A agora é: %i" %a)
print("O valor da variável B agora é: %i" %b)