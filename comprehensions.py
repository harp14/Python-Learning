# List comprehensions
values = []
for x in range(5):
    values.append(x * 2)

# The statements above can be replaced with the following
# [expression for item in items]
values = [x * 2 for x in range(5)]
print(values)

# These can also be for sets (data structure with no duplicates)
values = {x * 2 for x in range(5)}

# And dictionaries with their key value pairs
values = {x: x * 2 for x in range(5)}
print(values)

# And tuples
values = tuple(x * 2 for x in range(5))
print(values)
