'''
Generator expressions are used for large amounts of data where we don't want
to hold large amounts of data in memory.

They generate a new value in every iteration rather than storing everything in a variable.
'''
from sys import getsizeof

values = (x * 2 for x in range(1000))
print("1000 gen: ", getsizeof(values))


values = (x * 2 for x in range(100000))
print("100000 gen: ", getsizeof(values))

values = [x * 2 for x in range(100000)]
print("100000 list: ", getsizeof(values))
