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