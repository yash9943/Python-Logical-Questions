'''
 students = {"Alice":88, "Bob":95, "Charlie":92}
 Expected Output:
{'Bob': 95, 'Charlie': 92, 'Alice': 88}
'''

students = {"Alice":88, "Bob":95, "Charlie":92}

sorted_students = dict(sorted(students.items(), key=lambda item: item[1], reverse=True))

print(sorted_students)