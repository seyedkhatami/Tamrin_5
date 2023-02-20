from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Snake(Animal):
    
    def move(self):
        print("I'm moveinf ...")

    def sound(self):
        print("I'm sounding ...")

    def eat(self):
        print("I'm eating ...")

class Dog(Animal):

    def move(self):
        print("I'm moveinf ...")

    def sound(self):
        print("I'm sounding ...")

    def eat(self):
        print("I'm eating ...")

class Lion(Animal):

    def move(self):
        print("I'm moveinf ...")

    def sound(self):
        print("I'm sounding ...")

    def eat(self):
        print("I'm eating ...")

class Cat(Animal):

    def move(self):
        print("I'm moveinf ...")

    def sound(self):
        print("I'm sounding ...")

    def eat(self):
        print("I'm eating ...")

s = Snake()
s.eat()
s.move()
s.sound()

d = Dog()
d.eat()
d.move()
d.sound()

l = Lion()
l.eat()
l.move()
l.sound()

c = Cat()
c.eat()
c.move()
c.sound()
