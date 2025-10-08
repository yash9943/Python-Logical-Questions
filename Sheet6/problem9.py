'''
Q9. Write a Python program that reads a text file and counts how many words start with a vowel.
'''

vowels = 'aeiouAEIOU'
count = 0
v_word = [] 

with open('Sheet6/sample.txt', 'r') as file:
    text = file.read()
    words = text.split()
    
    for word in words:
        if word[0] in vowels:
            count += 1
            v_word.append(word)
            
print(v_word)
print(count)