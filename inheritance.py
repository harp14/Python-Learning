'''class Mammal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")

# As Mammal class is an argument in the class definition
# the methods within the class are inherited


class Dog(Mammal):
    def walk(self):
        print("Walk")


test = Dog()
# The age attribute defined within the Mammal class is also
# inherited and assigned to the object
print(test.age)




class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub

class Mammal(Animal):
    # If you define this constructor in the Mammal class it replaces the method
    # in the base class, if you still want access to the attributes from the base
    # class then you need to call the super() method as shown below
    def __init__(self):
        super().__init__()
        print("Mammal constructor")
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, Mammal))
# Statement below shows that all classes inherit from the object class
print(isinstance(m, object))
print(m.age)
print(m.weight)

o = object()
# If you then do o. you can see all the (magic) methods in the object class
'''

# Good example of inheritance
# Creating InvalidOperationError class below (this is a custom class)
# abc is abstract base class - we want Stream to only provide its functions
# to the other classes
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    # Using abstractmethod decorator
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")


# Can't create an instance of a class that contains an abstract method
# unless you override the abstract method within the class by making one
# with the same name - see MemoryStream()
stream = MemoryStream()
stream.open()
