'''
 Q5. Group Words by Length (10 Marks)
 Input: ['python','is','fun','to','learn']
 Output: {2: ['is','to'], 3: ['fun'], 5: ['learn'], 6: ['python']}
'''
list1 = ['python','is','fun','to','learn']
result = {}

for words in list1:
    length = len(words)
    if length not in result:
        result[length] = []
    result[length].append(words)
    
final_result = dict(sorted(result.items(),key=lambda item : item[0]))

print(final_result)