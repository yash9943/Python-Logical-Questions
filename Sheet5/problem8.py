'''
 Q8. Write a function that accepts a list of dictionaries representing employees (name,
 salary) and returns the top 3 highest-paid employees.
'''

employees = [
    {"name": "Yash", "salary": 70000}, 
    {"name": "Meet", "salary": 50000}, 
    {"name": "Akash", "salary": 60000}, 
    {"name": "Jenish", "salary": 80000}, 
    {"name": "Hit", "salary": 75000}
]

top = sorted(employees, key=lambda x : x['salary'],reverse=True)[:3]
print(top[0])
print(top[1])
print(top[2])
