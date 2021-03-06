# Classes: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: John, Mary, Jack


class Point:
    #  init short for initialise - can specify parameters for the class here (e.g. x and y)
    def __init__(self, x, y):
        self.x = x              # self is a reference to the current object
        self.y = y

    def move(self):
        print("Test")

    def draw(self):
        print("Draw")

    # The cls argument means it is a class method not an instance method, cls is a reference to the class itself not the object
    @classmethod    # This is a decorator and extends a behaviour
    def zero(cls):
        return cls(0, 0)


point1 = Point(10, 12)
point1.x = 11
print(point1.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I'm {self.name}")


john = Person('John')
john.talk()


# Inheritance - reusing methods from another class
class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):  # Inherit all methods from the Mammal class
    def bark(self):
        print("Woof")


class Cat(Mammal):  # Inherit all methods from the Mammal class
    pass    # Pass this line, do nothing


dog1 = Dog()
dog1.walk()
dog1.bark()


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


empl1 = Employee('Harry', 'Matharu', 30000)

print(
    f"Employee details:\nFirst name: {empl1.first}\nLast name: {empl1.last}\nSalary: {empl1.pay}")
