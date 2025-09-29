'''
dict1 = {'a':1, 'b':2, 'c':3}

output : {1:'a', 2:'b', 3:'c'}

'''

dict1 = {'a':1, 'b':2, 'c':3}

# dict1.update()
# print(dict1)

swapped_dict = {value: key for key, value in dict1.items()}
print(swapped_dict)

# for key, value in dict1.items():
#     swapped_dict = {value : key}
#     print(swapped_dict)
# print(swapped_dict)
