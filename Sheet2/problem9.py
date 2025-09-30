'''
 Q9. Fibonacci using Recursion and Memoization
 Write a function to return the nth Fibonacci number using recursion + memoization.
'''

memo = {}
def feb(n):
    if n in memo:
        return memo[n]
    else:
        if n == 1 or n == 0:
            value = n
        else:
            value = feb(n-1) + feb(n-2)
            
        memo[n] = value
        return value
    
for i in range(51):
    print(i, feb(i))