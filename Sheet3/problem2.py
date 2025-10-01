'''
Q2. Factorial without Recursion (5 Marks)
 Find factorial of a number using a loop (not recursion).
'''

n = int(input("Enter Number : "))
res = 1

for num in range(1,n+1):
    res *= num
    print(res)        