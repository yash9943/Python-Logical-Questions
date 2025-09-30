'''
 dict1 = {"a": 1, "b": 2}
 dict2 = {"b": 3, "c": 4}
 Output: {"a": 1, "b": 5, "c": 4}
'''

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
final = {}

for key, value in dict1.items():
    if key and value not in final:
        final[key] = value

for key, value in dict2.items():
    if key in final:
        final[key] += value
    else:
        final[key] = value
        
print(final)