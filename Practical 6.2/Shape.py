from Point import Point
from abc import ABC, abstractmethod
import math

class AbstractShape(ABC):
    def __init__(self, o: Point):
        self.o = o

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class AbstractCircle(AbstractShape):
    def __init__(self, o):
        super().__init__(o)   

class CircleByRadius(AbstractCircle):
    """Class to represent a circle on a graph"""
    
    def __init__(self, o: Point, r: int):
        """constructor for a rectangle, origin point is middle"""
        if not isinstance(o, Point):
            raise TypeError
        super().__init__(o)
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
        
class CircleByArea(AbstractCircle):
    """Class to represent a circle on a graph"""
    
    def __init__(self, o: Point, a: float):
        """constructor for a rectangle, origin point is middle"""
        if not isinstance(o, Point):
            raise TypeError
        super().__init__(o)
        self.a = a
        
    def __str__(self):
        """string representation of a circle"""
        return f'Circle has origin {self.o}, and an area of {self.a}'

    def __repr__(self):
        """formal string representation of a circle"""
        return f'Origin: {self.o}, Area: {self.a}'

    def area(self):
        """method to find the area of a circle"""
        return self.a
    
    def radius(self):
        """method to find the area of a circle"""
        return math.sqrt((self.a / math.pi))
        

    def perimeter(self):
        """method to find the perimeter of a rectangle"""
        return round(2*(self.radius())*math.pi, 2)

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        x_value = p.x - self.o.x
        y_value = p.y - self.o.y
        abc = x_value **2 + y_value**2
        if abc <= self.radius()**2:
            return True
        else:
            return False
        
class Rectangle(AbstractShape):
    """Class to represent a rectangle on a graph"""

    def __init__(self, o: Point, w, h):
        """constructor for a rectangle, origin point is middle"""
        super().__init__(o) #Origin
        self.w = w #Width
        self.h = h #Height
    
        pass

    def __str__(self):
        """string reprentation of a rectangle"""
        return f'Rectangle size is {self.w} by {self.h}, centre is {self.o.x},{self.o.y}'
        
        
    def __repr__(self):
        """formal string representation of a rectangle"""
        return f'{self.w} by {self.h} at {self.o}'
        

    def area(self):
        """method to find the area of a rectangle"""
        return self.w * self.h
        pass

    def perimeter(self):
        """method to find the perimeter of a rectangle"""
        return (2*self.w)+ (2 * self.h)
        pass

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        boundary_NE = Point(self.o.x + (1/2 *(self.w)), self.o.y + (1/2 *(self.h))) 
        boundary_NW = Point(self.o.x - (1/2 *(self.w)), self.o.y + (1/2 *(self.h))) 
        boundary_SE = Point(self.o.x + (1/2 *(self.w)), self.o.y - (1/2 *(self.h))) 
        boundary_SW = Point(self.o.x - (1/2 *(self.w)), self.o.y - (1/2 *(self.h))) 
        if p.x < boundary_NW.x:
            return False
        elif p.x > boundary_NE.x:
            return False
        elif p.y < boundary_SE.y:
            return False
        elif p.y > boundary_NE.y:
            return False
        else:
            return True
        
class Square(Rectangle):
    def __init__(self, o: Point, s):
        super().__init__(o, s, s)

    def __str__(self):
        """string reprentation of a square"""
        return f'Square size is {self.w} by {self.h}, centre is {self.o.x},{self.o.y}'
        
        
    def __repr__(self):
        """formal string representation of a square"""
        return f'{self.s} by {self.s} at {self.o}'
