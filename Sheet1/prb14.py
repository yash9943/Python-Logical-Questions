'''
 marks = {'Alice':88, 'Bob':45, 'Charlie':72, 'David':30}
 Expected Output: {'Alice': 88, 'Charlie': 72}
 '''
marks = {'Alice':88, 'Bob':45, 'Charlie':72, 'David':30}
result = {}
for key,values in marks.items():
    if values > 50:
        result[key] = values
        
print(result)