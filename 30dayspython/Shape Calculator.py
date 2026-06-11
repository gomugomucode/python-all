import math

class Circle :

    def __init__(self ,radius ):
        self.radius  = radius 

    def  area(self):
        if self.radius <= 0:
            raise ValueError(f"Radius cannot be negative. Got: {self.radius}") 
        area = math.pi * self.radius *self.radius 
        return f"The area of circle is {area}"

    def  perimeter(self):
        if self.radius <= 0:
            raise ValueError(f"Radius cannot be negative. Got: {self.radius}")
        perimeter = 2 * math.pi * self.radius  
        return f"The perimeter of circle is {perimeter}"
    
class Rectangle :

    def __init__(self ,width , height  ):
        self.width   = width 
        self.height   = height