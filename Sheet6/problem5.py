'''
Q5. Merge two dictionaries. If the same key appears, keep the higher value.
Example: {'a':2, 'b':3} + {'a':5, 'c':1} → {'a':5, 'b':3, 'c':1}
'''
dict1 = {'a':2, 'b':3}
dict2 = {'a':5, 'c':1}

res = dict1.copy()

for key, value in dict2.items():
    if key in res:
        res[key] = max(res[key], value)
    else:
        res[key] = value
print(res)