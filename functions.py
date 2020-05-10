# Example of a function that takes a parameter but doesn't return a value
def greet(name):
    print(f"Hi there {name}")
    print("Welcome aboard!")


# print("Hi there, what is your name?")
# name = input("Name: ")
# greet(name)


# Example of a function that returns a value
def multiply(first_number, second_number):
    return first_number * second_number


print(multiply(3, 15))

# Keyword argument example - makes it easier to understand arguments passed to function
print(multiply(first_number=3, second_number=15))


# Default function argument example - will increment by 1 by default unless otherwise specified
def increment(number, by=1):
    return number + by


print(increment(5, 0))


# Example of multiple arguments for function - xargs
def multiplymultiple(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiplymultiple(1, 2, 3, 4, 5))
