import math

from Point import Point
from Rectangle import Rectangle
from Circle import Circle
from Curve import Curve

        
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

# define a curve
def main():
        cur = Curve(Point(1,1),Point(2,4),Point(3,9))
        # cur = Curve(Point(1,1),(2,2)) # should raise a TypeError
        print(cur)
        print(cur.__repr__())
        # return a point/item
        print(cur[1]) # == print(cur.__getitem__(1))
        # return points/items i.e. subcurve
        print(cur[0:2]) # == print(cur.__getitem__(0:2))
        # update point
        cur[1] = Point(1,1) # == print(cur.__setitem__(1,Point(1,1)))
        # cur[1] = (1,1) # should raise a TypeError
        print(cur)


main()