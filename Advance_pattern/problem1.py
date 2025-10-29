"""
Diamond Pattern
 *
 ***
 *****
 *******
 *****
 ***
 *
"""
n = 5
for i in range(n+1):
    for j in range(n+1):
        if j < i:
            print('*', end='')
    print('')
for i in range(n+1):
    for k in range(n+1):
        if k-1 > i:
            print('*', end='')
    print('')
    