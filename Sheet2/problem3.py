'''
 Input: "developer"
 Output: Vowels: 4, Consonants: 5
 '''
 
string = "developer"
vowels_char = ['a','e','i','o','u']
vowels = 0
consonants = 0

for i in string:
    if i in vowels_char:
        vowels += 1
    else:
        consonants += 1     
        
print(f"Vowels : {vowels}, Consonants : {consonants}")