from Point import Point
import math

class Circle():
    """Class to represent a circle on a graph"""
    
    def __init__(self, o, r):
        """constructor for a rectangle, origin point is middle"""
        if not isinstance(o, Point):
            raise TypeError
        self.o = o
        self.r = r
        
    def __str__(self):
        """string representation of a circle"""
        return f'Circle has origin {self.o}, and a radius of {self.r}'

    def __repr__(self):
        """formal string representation of a circle"""
        return f'Origin: {self.o}, Radius: {self.r}'

    def area(self):
        """method to find the area of a circle"""
        return round(math.pi*(self.r**2), 2)
        

    def perimeter(self):
        """method to find the perimeter of a rectangle"""
        return round(2*self.r*math.pi, 2)

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        x_value = p.x - self.o.x
        y_value = p.y - self.o.y
        abc = x_value **2 + y_value**2
        if abc <= self.r**2:
            return True
        else:
            return False
        