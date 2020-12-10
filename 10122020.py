import math

a = int(input('Первое число '))

b = int(input('Второе число '))

if math.gcd(a, b) > 1:

   print('взаимно простые')

else:

   print('не взаимно простые')