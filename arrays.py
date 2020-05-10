# Only use arrays instead of lists if performance issues in program
from array import array

# Use the following to find right type code: https://docs.python.org/3/library/array.html
# The type code specifies what type of data you are entering into the array
# You can not add any other type of data into the array other than specified type code
numbers = array("i", [1, 2, 3])
numbers.append(4)
print(list(numbers))
