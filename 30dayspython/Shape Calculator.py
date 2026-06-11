import math

class Circle :

    def __init__(self ,radius ):
        self.radius  = radius 

    def  area(self):
        area = math.pi * self.radius *self.radius 
        return f"The area of circle is {area}"

    def  perimeter(self):
        perimeter = 2 * math.pi * self.radius  
        return f"The perimeter of circle is {perimeter}"
        