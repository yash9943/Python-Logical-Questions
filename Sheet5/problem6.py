'''
 Q6. Write a Python function to find the longest substring without repeating characters.
 Example: "abcabcbb" -> "abc"
'''

string = "abcabcbb"
res = ''

for i in string:
    if i not in res:
        res += i
        
print(res)