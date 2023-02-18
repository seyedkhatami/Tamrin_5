#1 : abstract class method


from abc import ABC

class MyABC(ABC):
    pass

MyABC.register(tuple)
assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)

class Foo:
    def __getitem__(self, index):
        ...
    def __len__(self):
        ...
    def grt_iterator(self):
        return iter(self)
    
class MyIterable(ABC):

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iterator(self):
        return self.__iter__()
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
            return NotImplemented
        
MyIterable.register(Foo)


#2 : abstract method


class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        print("Some implementation!")

class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")

x = AnotherSubclass()
x.do_something


#3 : abstract property


from abc import ABCMeta, abstractmethod

class Base(object):

    __metaclass__ = ABCMeta
    def __init__(self, str_dir_config):
        self.str_dir_config = str_dir_config

    @abstractmethod
    def _do_stuff(self, signals):
        pass

    @property
    @abstractmethod
    def name(self):
        """This property will be supplied by the inheriting classes individually"""
        pass

class Base1(Base):
    __metaclass__ = ABCMeta


    def __init__(self, str_dir_config):
        super(Base1, self).__init__(str_dir_config)

    def _do_stuff(self, signals):
        print("Base_1 does stuff")

class C(Base1):

    @property
    def name(self):
        return "class C"
    
if __name__ == "__main__":
    b1 = Base1("abc")



#4 : abstract static method


from abc import ABC, abstractstaticmethod


class abstractstatic(staticmethod):


    def __init__(self, function):
        super(abstractstatic, self).__init__(function)
        function.__isabstractmethod__ = True
    ___isabstractmethod__ = True

class A(object):

    @abstractstatic
    def test():
        print(5)