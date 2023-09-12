"""
Write a Python program to create a class representing a Circle. 
Include methods to calculate its area and perimeter. 
"""
import math
class Circle():
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * pow(self.radio, 2)
    
    def perimeter(self):
        return math.pi * (self.radio) * 2
    
my_circle = Circle(4)
print(my_circle.area())
print(my_circle.perimeter())
