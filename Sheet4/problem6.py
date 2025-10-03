'''
 Q6. Write a program to count how many times each element appears in a list.
 Example: [1,2,2,3,1] → {1:2, 2:2, 3:1}
'''
list1 = [1,2,2,3,1]
dict1 = {}

for i in list1:
    if i not in dict1:
        dict1[i] = 0
    dict1[i] += 1

print(dict1)
        