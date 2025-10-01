'''
 Q3. Sum of Even Numbers in List (10 Marks)
 Input: [1,2,3,4,5,6] → Output: 12
'''

list1 = [1,2,3,4,5,6]
evensum = 0
for num in list1:
    if num % 2 == 0:
       evensum += num
       
print(evensum)