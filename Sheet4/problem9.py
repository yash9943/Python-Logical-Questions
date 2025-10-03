'''
Q9. Write a program to read a text file and print all lines in uppercase.
'''
with open(r'Sheet4\sample.txt', 'w') as file:
    file.write("hello world\n")
    file.write("python programming\n")
    file.write("file handling test\n")

with open(r'Sheet4\sample.txt', 'r') as file:
    for line in file:
        print(line.strip().upper())
