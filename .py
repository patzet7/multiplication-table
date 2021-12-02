#Multiplication table from 1 to 10

import random
print('Multiplication table')
a = random.randint(1,10)
b = random.randint(1,10)

result = input('Give the result of the multiplication: ' + str(a) + ' * ' + str(b) + ' = ')
if int(result) == a*b:
  print('Good job!')
else:
  print('Try again')
