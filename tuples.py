# Tuples - these can not be changed; you can only find information about them
coordinates = (1, 2, 3)

# Tuples examples
point = (1, 2) + (3, 4)
print(point)

point = (1, 2) * 3
print(point)

point = (1, 2, 3)

# Use tuple function to convert iterables to tuples (e.g. dictionaries and strings)
print(tuple([1, 2, 3]))
print(tuple("Hello"))
print(point[0:2])

# Can unpack tuples to variables:
x, y, z = point

# Can check if items exist within tuple
if 10 in point:
    print("Exists")
else:
    print("Does not exist")
