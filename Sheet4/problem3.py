'''
Q3. Write a program to find the sum of digits of a given number.
 Example: 1234 → 10
'''

num = int(input("Enter Number : "))
result = 0
for i in range(1,num+1):
    result = result + i
    
print(result)