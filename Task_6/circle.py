import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        area = math.pi * (self.radius ** 2)
        return area
    
    def perimeter(self):
        perimeter = math.pi * (self.radius * 2)
        return perimeter
       
