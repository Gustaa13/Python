a = input('Digite o texto A: ')
b = input('Digite o texto B: ')

print ('Texto A dividido em duas partes: {} e {}'.format(a[:(len(a) // 2)], a[(len(a) // 2):]))
print ('Texto B dividido em duas partes: {} e {}'.format(b[:(len(b) // 2)], b[(len(b) // 2):]))
print ('{} + {} = {}'.format(a[:(len(a) // 2)], b[(len(b) // 2):], a[:(len(a) // 2)] + b[(len(b) // 2):]))
print ('{} + {} = {}'.format(a[(len(a) // 2):], b[:(len(b) // 2)], a[(len(a) // 2):] + b[:(len(b) // 2)]))
print ('{} + {} + {} + {} = {}'.format(a[0], b[1], a[len(a) - 1], b[len(b) - 1], a[0] + b[1] + a[len(a) - 1] + b[len(b) - 1]))