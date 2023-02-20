from abc import ABC, abstractmethod, abstractproperty

class Polygon(ABC):
    def __init__(self, x):
        self.x = x

    @abstractproperty
    def sides(self):
        return self.x

class Triangle(Polygon):
    def __init__(self, x):
        super().__init__(x)

    @property
    def sides(self):
        return self.x
    
class Pentagon(Polygon):
    def __init__(self, x):
        super().__init__(x)

    @property
    def sides(self):
        return self.x
    
class Hexagon(Polygon):
    def __init__(self, x):
        super().__init__(x)

    @property
    def sides(self):
        return self.x
    
class Quadrilateral(Polygon):
    def __init__(self, x):
        super().__init__(x)

    @property
    def sides(self):
        return self.x
    
t = Triangle(3)
t.sides()

p = Pentagon(5)
p.sides()

h = Hexagon(6)
h.sides()

q = Quadrilateral(4)
q.sides
