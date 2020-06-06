class Mammal:
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
