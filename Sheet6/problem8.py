'''
Q8. Write a Python program to print the Fibonacci sequence up to n terms using iteration (not recursion).
'''

n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
 