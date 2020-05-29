# Example for performing arithmetic operations on Point objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(f"{combined.x},{combined.y}")


# Example for comparison of point objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # If this method isn't defined then the result of the expression
    # is false because Python compares the memory locations rather
    # than the values themselves
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Defining greater than magic method here to override the behaviour
    # of Python comparison which will say that point objects cannot be compared
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
print(point > other)

# Use the following site as a resource for learning about magic methods: https://rszalski.github.io/magicmethods

# Example for changing the behavior of Python when returning locations of a point


class Point:
    # These are instance methods
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# If you try to print the point object without the __str__ method defined
# then an error will be thrown because AX by default prints the memory address,
# we are overriding this behaviour by re-defining the __str__ method
point = Point(1, 2)
print(point)
