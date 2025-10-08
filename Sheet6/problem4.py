'''
Q4. Write a Python program to find the second largest number in a list.
Example: [10, 20, 4, 45, 99] → 45
'''

list1 = [10, 20, 4, 45, 99]
list1.sort(reverse=True)

print(list1[1])