'''
 lst = [1,2,2,3,4,4,5]
 Expected Output: [1, 2, 3, 4, 5]
'''
lst = [1,2,2,3,4,4,5]
# lst.sort()

# print(lst)

res = []
for i in lst:
    if i not in res:
        res.append(i)
        
print(res)