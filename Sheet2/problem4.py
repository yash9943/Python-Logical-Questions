'''
 Input: [1, 2, 2, 3, 4, 4, 5]
 Output: [1, 2, 3, 4, 5
'''
list1 = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for i in list1:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)