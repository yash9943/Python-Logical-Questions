'''
 Q8. Write a function to return the factorial of a number using recursion.
'''

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))
print(fact(0))
print(fact(1))
print(fact(10))
