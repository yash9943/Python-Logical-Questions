'''
 Input: "I love Python"
 Output: "Python love I"
'''

string = "I love Python"

final = string[7:13] +" "+string[2:6] +" "+ string[0]
print(final)

# word = string.split()
# reversed_words = word[::-1]
# final = " ".join(reversed_words)
# print(final)