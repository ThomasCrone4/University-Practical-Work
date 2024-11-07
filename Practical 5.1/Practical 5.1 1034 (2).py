import math

class Point():
    """class to represent a point on a graph"""

    def __init__(self, x, y):
        """constructor for a point"""
        self.x = x
        self.y = y
       

    def __str__(self):
        """string representation of a point"""
        return f'Point X: {self.x}, Point Y: {self.y}'
        

    def __repr__(self):
        """formal string representation of a point"""
        return f'Point("{self.x}",{self.y})'

    # define a point
"""def main():
    p = Point(2,1)
    # p = Point("2",1) # should raise a TypeError
    print(p)  == print(p.__str__())
    print(p.__repr__())"""


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
        
    # define a rectangle
"""def main():
    r = Rectangle(Point(1,1),2,3)
    # r = Rectangle((1,1),2,3) # should raise a TypeError
    print(r)
    print(r.__repr__())
    print("{} -> area={}, peri={}".format(r, r.area(), r.perimeter()))
    # should be true
    print(Point(1,1) in r) # == print(r.__contains__(Point(1,1)))
    print(Point(1,0) in r)
    # should be false
    print(Point(0,3) in r)
    print(Point(3,0) in r)"""

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
        


# define a circle
"""def main():
        cir = Circle(Point(1,1),2)
        # c = Circle((1,1),2) # should raise a TypeError
        print(cir)
        print(cir.__repr__())
        print("{} -> area={}, peri={}".format(cir, cir.area(), cir.perimeter()))
        # should be true
        print(Point(1,1) in cir) # == print(cir.__contains__(Point(1,1)))
        print(Point(1,0) in cir)
        # should be false
        print(Point(0,3) in cir)
        print(Point(3,0) in cir)"""

class Curve():
    """Class to represent a list of points on a graph"""
    
    def __init__(self,*inputs):
        """constructor for a curve"""
        self.items = []
        for input in inputs:
            self.append_if_valid(input)
    
    
    def append_if_valid(self,item):
        """add a new point object to the curve""" 
        if isinstance (item, int)      
        pass

    def __str__(self):
        """string representation of a curve"""
        return f'Curve has points: {}'.format(self.items)
        pass

    def __repr__(self):
        """formal string representation of a curve"""
        pass

    def __getitem__(self,index):
        """get point(s) in curve"""
        if isinstance*index, int):
            return self.items[index]
        else:
            return Curve(*self.items[index])
        pass
        
    def __setitem__(self,index,item):
        """update curve with given point value"""
        if not isintance(item,Point):
            raise TypeError ("Must be a point")
        pass

main()