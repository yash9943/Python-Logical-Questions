'''
 n = 5
 Expected Output:
 *
 **
 ***
 ****
 *****
'''
 
n = 5
for i in range(n):
    for j in range(n):
        if j < i:
            print('*', end='')
    print('*')