class ShapesList:
    def __init__(self):
        self.shapes = []
        print("In init")
        
    def add(self, s):
        print(s)
        self.shapes.append(s)
    
    def areas(self):
        return [shapes.area() for shapes in self.shapes]

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
        
    def area(self):
        return self.base * self.height / 2.0
    
class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.height = w
    
    def area(self):
        return self.length * self.height / 2.0

class Circle:
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return 3.14 * self.radius * self.radius
    