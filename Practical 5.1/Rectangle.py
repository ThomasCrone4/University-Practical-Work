from Point import Point

class Rectangle():
    """Class to represent a rectangle on a graph"""

    def __init__(self, o, w, h):
        """constructor for a rectangle, origin point is middle"""
        self.o = o #Origin
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