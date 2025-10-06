'''
 Q2. Write a program to check if two strings are anagrams of each other.
 Example: "listen" & "silent" -> True
'''
string1 = "listen"
string2 = "silent"

if sorted(string1) == sorted(string2):
    print("True")
else:
    print("False")