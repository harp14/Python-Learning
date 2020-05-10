# Importing modules
import converters                   # Importing all functions
from converters import kg_to_lbs    # Press ctrl + space to see the various importable functions

print(converters.kg_to_lbs(10))     # If importing all functions have to do this
print(kg_to_lbs(10))                # If importing particular function can do this


# Creating and importing from a package
from utils import find_max

test_array = [2,3,4,5,2]
result = find_max(test_array)
print(result)


# Importing from a package
from ecommerce import shipping                  # To import an entire module
shipping.calc_shipping()                        # Specifying function to use later on

from ecommerce.shipping import calc_shipping    # To import a specific function from a module
calc_shipping()