'''
n = 5
Expected Output:
     *
    ***
   *****
  *******
 *********
'''

n = 5

for i in range(n+1):
    for j in range(n+1-i-1):
        print(end=" ")
    for j in range(i):
        print("*", end=" ")
    print()