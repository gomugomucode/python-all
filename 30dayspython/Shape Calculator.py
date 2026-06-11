import math

class Circle:
    # Class attribute to track total circles
    shapes_created = 0

    def __init__(self, radius):
        # Constraint: Validate all dimensions in __init__ using static method
        if not self.is_valid_dimension(radius):
            raise ValueError("radius must be positive")
        self.radius = radius
        # Must increment via the Class name to update the shared counter
        Circle.shapes_created += 1

    def area(self):
        # Constraint: Raw float output rounded to 2 decimal places
        return round(math.pi * (self.radius ** 2), 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def __str__(self):
        return f"Circle(r={self.radius})"

    @staticmethod
    def cm_to_inch(cm):
        # 10 cm should yield 3.937 as shown in the example
        return round(cm * 0.3937, 3)

    @staticmethod
    def is_valid_dimension(val):
        return val > 0

    @classmethod
    def total_created(cls):
        # cls refers to the Circle class dynamically
        return f"Circles created: {cls.shapes_created}"


class Rectangle:
    # Class attribute to track total rectangles
    shapes_created = 0

    def __init__(self, width, height):
        # Validate both individual dimensions separately
        if not self.is_valid_dimension(width) or not self.is_valid_dimension(height):
            raise ValueError("dimensions must be positive")
        self.width = width
        self.height = height
        Rectangle.shapes_created += 1

    def is_square(self):
        return self.width == self.height

    def area(self):
        return round(self.width * self.height, 2)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"

    @staticmethod
    def cm_to_inch(cm):
        return round(cm * 0.3937, 3)

    @staticmethod
    def is_valid_dimension(val):
        return val > 0

    @classmethod
    def total_created(cls):
        return f"Rectangles created: {cls.shapes_created}"

if __name__ == "__main__":
    c1 = Circle(5)
    c2 = Circle(3)
    c3 = Circle(10) 
    
    r1 = Rectangle(4, 6)
    r2 = Rectangle(5, 5)

   