'''
Q3. Given a string, find the first repeated character.
Example: "abcbd" → 'b'
'''
string = "abcbd"
nonrep = ''
reapted = ''

for i in string:
    if i not in nonrep:
        nonrep += i
    else:
        reapted += i
        break
print(reapted)