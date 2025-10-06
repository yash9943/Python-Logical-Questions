'''
 Q5. Given a list of integers, return the two numbers whose sum is closest to zero.
 Example: [-8, -66, -60, 10, 8, 50] -> [-60, 50]
'''

list1 = [-8, -66, -60, 10, 8, 50]
list1.sort()

closest_sum = float("inf")  # start with infinity
pair = (0, 0)  # to store result

for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        current_sum = list1[i] + list1[j]
        
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            pair = (list1[i], list1[j])

print(pair)
