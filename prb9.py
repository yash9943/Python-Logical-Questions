'''
 list1 = [1,2,3]
 list2 = [2,3,4]
 Expected Output: [1, 2, 3, 4]
'''

list1 = [1,2,3]
list2 = [2,3,4]

final = []

for i in list1:
    if i not in final:
        final.append(i)
        
for i in list2:
    if i not in final:
        final.append(i)
        
print(final)