# Example of multiple arguments for function - xargs
# Using a single asterisk allows you to pass multiple values into the parameter


def multiplymultiple(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiplymultiple(1, 2, 3, 4, 5))


# When using double asterisks we can pass multiple key value pairs and Python will
# automatically package them into a dictionary
def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="Harry", age=22)
