t1 = input('Texto 1: ')
t2 = input('Texto 2: ')
t3 = input('Texto 3: ')

if t1 > t2:
    t = t2
    t2 = t1
    t1 = t
if t1 > t3:
    t = t3
    t3 = t1
    t1 = t
if t2 > t3:
    t = t3
    t3 = t2
    t2 = t
print ('1°. ' + t1)
print ('2°. ' + t2)
print ('3°. ' + t3)