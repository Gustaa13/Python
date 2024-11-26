d = int(input('Números de dias: '))

s = (d // 7) 
d1 = round(((d / 7) - (d // 7)) * 7)

if d == 0:
    print ('0 dias equivale à nenhum dia.')
elif d == 1:
    print ('1 dia equivale à 1 dia!')
elif d < 7:
    print ('{} dias equivalem à {} dias!'.format(d, d))
elif d == 7:
    print ('7 dias equivalem à 1 semana!')
elif d == 8:
    print ('8 dias equivalem à 1 semana e 1 dia!')
elif s == 1 and d1 > 1:
    print ('{} dias equivalem à 1 semana e {} dias!'.format(d, d1))
elif s > 1 and d1 == 0:
    print ('{} dias equivalem à {} semanas!'.format(d, s))
elif s > 1 and d1 == 1:
    print ('{} dias equivalem à {} semanas e 1 dia!'.format(d, s))
elif s > 1 and d1 > 1:
    print ('{} dias equivalem à {} semanas e {} dias!'.format(d, s, d1))