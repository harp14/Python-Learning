# Sets are a data structure that is an unordered collection with no duplicates

numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)  # Convert list to a set
print(uniques)

first = set(numbers)

second = {1, 5}  # Note that sets are specified using curly brackets
second.add(4)
print(second)   # You can add to a set like in lists

# Union two sets
print(first | second)

# Get items that are only in both sets
print(first & second)

# Get the difference between two sets
print(first - second)

# Items that are either in the first or second set but not both
print(first ^ second)
