'''
 Q5. Given a dictionary, print all keys and values.
 Example: {'a':1, 'b':2} → Keys: a, b; Values: 1, 2
'''

dict1 = {'a':1, 'b':2} 

# for key, value in dict1.items():
#     return key value

key = list(dict1.keys())
value = list(dict1.values())

print(f"Keys : {key}, Values : {value}")