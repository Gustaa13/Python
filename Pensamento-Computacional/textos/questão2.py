import math

x, y, z = int

x = int(input('x?'))
y = int(input('y?'))
z = int(input('z?'))

print ('({}^2 + {}^2 + {}^2)^1/3 = {}'.format(x, y, z, (x**2 + y**2 + z**2) ** (1 / 3)))
print ('{}^{} + {}^{} = {}'.format(x, y, y, z, (x**y) + (y**z)))
print ('sin({}^2 + {}^2) + cos({}^2 + {}^2) = {}'.format(x, y, y, z, (math.sin(x**2 + y**2) + math.cos(y**2 + z**2))))
print ('(log {} + log {} + log {}) ^ ({} + {} + {}) = {}'.format(x, y, z, x, y, z, (math.log10(x) + math.log10(y) + math.log10(z)) ** (x + y + z)))