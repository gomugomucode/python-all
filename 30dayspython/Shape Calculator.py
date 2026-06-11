import math

class Circle :
    shapes_created = 0

    def __init__(self ,radius ):
        self.radius  = radius 
        self.shapes_created += 1

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
    shapes_created = 0

    def __init__(self ,width , height  ):
        self.width   = width 
        self.height   = height
        self.shapes_created += 1

    def is_square(self):
        if self.width == self.height :
            return True
        else :
            return False

    def  area(self):
        if self.width or self.height   <= 0:
            raise ValueError(f"Dimension  cannot be negative. Got: {self.radius}") 
        area = math.pi * self.radius *self.radius 
        return f"The area of circle is {area}"

    def  perimeter(self):
        if self.radius <= 0:
            raise ValueError(f"Dimension  cannot be negative. Got: {self.radius}")
        perimeter = 2 * math.pi * self.radius  
        return f"The perimeter of circle is {perimeter}"

    @staticmethod 
    def cm_to_inch(a):
        return(f"The value in inch is {a * 0.3937 }inch")

    
     @staticmethod 
    def is_valid_dimension(val):
        if val < 0:
            return f"Dimension cannot be negative. Got: {val}"  
        return True 

        