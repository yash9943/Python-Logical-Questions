'''

Q7. Write a function that returns all numbers between 1 and 100 that are divisible by both 3 and 5.
'''
res = []
def find_numbers():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            res.append(i)
    return res
    
print(find_numbers())


# return [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]