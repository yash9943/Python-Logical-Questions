'''
 Q4. Pascal’s Triangle
from math import factorial
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1
'''

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
n = 5
for i in range(n):
    print(' ' * (n - i), end='')
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=' ')
    print()

