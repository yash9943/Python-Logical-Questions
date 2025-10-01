'''
 Q6. Sort Dictionary by Values (10 Marks)
 Input: {'a':3,'b':1,'c':2}
 Output: {'b':1,'c':2,'a':3}
'''

dict1 = {'a':3,'b':1,'c':2}

sorted_dict = dict(sorted(dict1.items(), key= lambda item : item[1]))

print(sorted_dict)