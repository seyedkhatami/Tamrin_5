from abc import ABC, abstractmethod

adadepi = 3.14

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def masahat(self):
        return self.x * self.y

    @abstractmethod
    def mohit(self):
        return (self.x + self.y) * 2

    @abstractmethod
    def __str__(self):
        return self.x, self.y

class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)

    def masahat(self):
        return self.x * self.y
    
    def mohit(self):
        return (self.x + self.y) * 2
    
    def __str__(self):
        return self.x, self.y

class Square(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)

    def masahat(self):
        return self.x * self.y
    
    def mohit(self):
        return (self.x + self.y) * 2
    
    def __str__(self):
        return self.x, self.y

class Triangle(Shape):
    def __init__(self, h1, h2, b): # h1 : ertefa1, h2 : ertefa2, b : ghaede
        self.h1 = h1
        self.h2 = h2
        self.b = b

    def masahat(self):
        return (self.b * self.h1 or self.h2) / 2
    
    def mohit(self):
        return self.h1 + self.h2 + self.b
    
    def __str__(self):
        return self.h1, self.h2, self.b

class Circle(Shape):
    def __init__(self, r, w):
        self.r = r # shoae
        self.w = w # ghotr

    def masahat(self):
        return adadepi * self.r * self.r
    
    def mohit(self):
        return adadepi * self.w
    
    def __str__(self):
        return self.r, self.w

class Diamond(Shape):
    def __init__(self, z, q1, q2):
        self.z = z # 1 zele
        self.q1 = q1 # ghotr kochak
        self.q2 = q2 # ghotr bozorg

    def masahat(self):
        return (self.q1 * self.q2) / 2

    def mohit(self):
        return self.z * 4
    
    def __str__(self):
        return self.z, self.q1, self.q2

r = Rectangle(10, 15)
r.mohit()
r.masahat()

s = Square(10, 20)
s.masahat()
s.mohit()

t = Triangle(5, 10, 15)
t.masahat()
t.mohit()

c = Circle(5, 7)
c.masahat()
c.mohit()

d = Diamond(10, 6, 4)
d.masahat()
d.mohit()
