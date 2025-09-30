'''
 Q10.File Handling – Word Count
 Write a program to read a text file and count how many times each word appears.
'''
word_count = {}
with open(r'D:\Problem Solving\Sheet2\test.txt') as file:
    for line in file:
        words = line.split()
        # print(words)
        for word in words:
            if word in word_count:
                word_count[word] = word_count[word]+1
            else:
                word_count[word] = 1
                
print(word_count)