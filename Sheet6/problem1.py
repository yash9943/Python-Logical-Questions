'''
Q1. Write a function to check whether a string is a palindrome without using slicing.
Example: "madam" → True
'''

string = "madam"
revstr = string[::-1]

if string == revstr:
    print("True")
else:
    print("False")