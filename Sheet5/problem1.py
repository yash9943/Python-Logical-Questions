'''
Q1. Write a Python function that returns the first non-repeating character in a string.
 Example: "aabbcde" -> c
'''

string = "aabbcde"
res = ''

for i in string:
    if string.count(i) == 1:
        res = i
        break

print(res)
