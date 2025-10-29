'''
Method Overloading in Python
'''
# USING Default Arguments
class math():
    def add(self, a=0, b=0, c=0):
        return a+b+c
    
obj = math()
print(obj.add(2, 3))        # Output: 5
print(obj.add(2, 3, 4))     # Output: 9

# USING Variable Length Arguments
class math():
    def add(self, *args):
        return sum(args)

obj = math()
print(obj.add(2, 3))        # Output: 5
print(obj.add(2, 3, 4))     # Output: 9