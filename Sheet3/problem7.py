'''
 Q7. Student Class (15 Marks)
 - Attributes: name, marks (list of numbers).
 - Methods: calculate average, check pass/fail (pass if average ≥ 40).
'''

class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def average(self):
        return sum(self.marks) / len(self.marks)
    
    def pass_fail(self):
        avg = self.average()
        if avg >= 40:
            return "Pass"
        else:
            return "Fail"

stud1 = Student('Yash',[30,25,60])
print("Average : ", stud1.average())
print("Result : ", stud1.pass_fail())

stud2 = Student('Yaish',[55,45,80])
print("Average : ", stud2.average())
print("Result : ", stud2.pass_fail())
