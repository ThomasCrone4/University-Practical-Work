from Point import Point


class Curve():
    """Class to represent a list of points on a graph"""
    
    def __init__(self,*inputs):
        """constructor for a curve"""
        self.items = []
        for i in inputs:
            self.append_if_valid(i)
    
    
    def append_if_valid(self,item):
        """add a new point object to the curve""" 
        if not isinstance (item, Point):  
            raise TypeError("Curves only take point objects")   
        self.items.append(item)

    def __str__(self):
        """string representation of a curve"""
        return "Curve has points:{}".format(self.items)
        

    def __repr__(self):
        """formal string representation of a curve"""
        s = ", "
        s = s.join( [repr(x) for x in self.items])
        return "Curve({})".format(s)

    def __getitem__(self,index):
        """get point(s) in curve"""
        if isinstance(index, int):
            return self.items[index]
        else:
            return Curve(*self.items[index])
        pass
        
    def __setitem__(self,index,item):
        """update curve with given point value"""
        if not isinstance(item,Point):
            raise TypeError ("Must be a point")
        self.items[index] = item
    
