'''
dict1 = {'a':1, 'b':2}
 dict2 = {'b':3, 'c':4}
 Expected Output: {'a': 1, 'b': 3, 'c': 4}
'''

dict1 = {'a':1, 'b':2}
dict2 = {'b':3, 'c':4}

dict1.update(dict2)
print(dict1)