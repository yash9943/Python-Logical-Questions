'''
 Q4. Implement a function to flatten a nested list without using recursion.
 Example: [1, [2, [3, 4]], 5] -> [1,2,3,4,5]
'''

list1 = [1, [2, [3, 4]], 5]
res = []

while list1:
    ele = list1.pop(0)
    if isinstance(ele, list):
        list1 = ele + list1
    else:
        res.append(ele)

print(res)