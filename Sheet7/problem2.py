'''
Method overriding in Python
'''

class Parent():
    def show(self):
        return "Parent class method"
    
class Child(Parent):
    def show(self):
        return "Child class method"
    
obj = Child()
print(obj.show())  # Output: Child class method

ob = Parent()
print(ob.show())  # Output: Parent class method