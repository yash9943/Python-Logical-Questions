'''
Q6. Write a Python program to remove duplicates from a list while maintaining order.
'''
list1 = [1, 2, 2, 3, 4, 4, 5]
res = []

for i in list1:
    if i not in res:
        res.append(i)
        
print(res)