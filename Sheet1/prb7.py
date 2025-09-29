'''
 lst = [1,2,3,4,5,6]
 Expected Output: [4, 16, 36]
'''

lst = [1,2,3,4,5,6]

res = [i*i for i in lst if i%2==0]

print(res)
        