'''
Q7. Create a Car class with attributes brand and speed. Write a method display() to print car
 details.
'''

class Car():
    def __init__(self,car,brand,speed):
        self.car = car
        self.brand = brand
        self.speed = speed
        
    def display(self):
        print(f"Car name : {self.car},\nCar brand : {self.brand},\nSpeed : {self.speed}\n")
        
car1 = Car("Innova","Toyota",80)
car2 = Car("X7","BMW",150)

car1.display()
car2.display()