'''
sentence = "python is easy and python is fun"
 Expected Output:
 {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'fun': 1}
 
'''
sentence = "python is easy and python is fun"
res = {}

word = sentence.split()
# print(word)

for i in word:
    if i not in res.keys():
        res[i] = 0
    res[i] = res[i] + 1
    
print(res)