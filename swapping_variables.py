# Usual method for swapping varibles:

x = 10
y = 11
# Create a new variable (z) to store a value
z = x
x = y
y = z

print(f"x is {x}")
print(f"y is {y}")

# Easier way to do this in Python:
x = 10
y = 11
x, y = y, x  # This is the same as unpacking a tuple

print(f"x is {x} and y is {y}")
