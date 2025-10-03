'''
Q4. Write a program to find the maximum and minimum in a list.
 Example: [4, 7, 1, 9, 0] → Max: 9, Min: 0
'''
list1 = [4, 7, 1, 9, 0]

list1.sort()
# print(list1)
print(f"Max : {list1[-1]}, Min : {list1[0]}")