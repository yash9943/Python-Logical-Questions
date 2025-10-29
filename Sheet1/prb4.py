'''
   *
  ***
 *****
  ***
   *
'''
n = 3
for i in range(1,n+1):
    for j in range(n+1-i-1):
        print(end=" ")
    for j in range(i):
        print('*', end=" ")
    print()
    
for k in range(n,0,-1):
    for j in range(n-k+1):
        print(end=' ')
    for j in range(k-1):
        print('*', end=' ')
    print()

