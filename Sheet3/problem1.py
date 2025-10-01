'''
 Q1. Palindrome Check (5 Marks)
 Write a function to check if a given string is a palindrome.
 Input: "level" → Output: True
'''

str = "level"
rev = str[::-1]
# result = False
if str == rev:
    result = True
else:
    result = False
    
print(result)