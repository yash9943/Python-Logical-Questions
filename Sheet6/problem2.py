'''
Q2. Write a Python program to count the frequency of each character in a string.
Example: "hello" → {'h':1, 'e':1, 'l':2, 'o':1}
'''
string = "hello"
res = {}

for i in string:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1
        
print(res)