# Operators and augmented assignment operator
print(10 / 3)   # This returns a floating point number
print(10 // 3)  # This returns an integer
print(10 % 3)   # This returns the remainder of a division
print(10 ** 3)  # This is exponent which is the power so this is 10 to the power of 3
x = 10
x = x + 3
x += 3  # Augmented assignment operator - same as line above
x -= 3  # Augmented assignment operator - same as line above
print(x)


# Useful functions for working with numbers
import math
print(round(2.9))       # Round number
print(abs(-2.9))        # Absolute value - always returns positive representation of value
print(math.ceil(2.2))   # Ceiling of a number
print(math.floor(2.9))  # Floor of a number


# Circle area calculator
import math
print('Circle calculator')
radius = input('Enter radius: ')
print (math.pi * (float(radius) ** 2))