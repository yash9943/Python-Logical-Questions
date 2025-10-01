'''
 Q9. JSON File Handling (15 Marks)
 Write a program to store a dictionary into a JSON file and then read it back.
'''
import json
import os

folder = "Sheet3"
os.makedirs(folder, exist_ok=True)

path = os.path.join(folder, "students.json")

data = {
    "name":"yash",
    "age":21,
    "course":"python",
    "marks":[50,60,70]
}

with open(path,'w') as f:
    json.dump(data, f, indent=4)
    
with open(path,'r') as f:
    load_data = json.load(f)
print(load_data)