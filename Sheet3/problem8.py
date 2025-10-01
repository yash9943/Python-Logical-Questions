'''
 Q8. Lambda with Filter (10 Marks)
 Write a program to filter out even numbers from a list using lambda and filter()
'''

n = int(input("Enter Number : "))
even = lambda n : [ i for i in range(n) if i%2 == 0]
print(even(n))