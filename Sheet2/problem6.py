'''
 Input: "python is great and python is simple"
 Output: {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'simple': 1}
'''
sentanse = "python is great and python is simple"

res = {}
words = sentanse.split()

for word in words:
    if word not in res.keys():
        res[word] = 0
    res[word] +=1
    
print(res)