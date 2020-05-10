# Lists
from collections import deque
names = ['Harry', 'Sophie', 'Bob', 'Kevin', 'Steve']
print(names[0:2])
names[0] = 'Harpreet'
print(names)


# Creating a list with multiple same values
zeros = [0] * 100
print(zeros)


# Combining lists
letters = ["a", "b", "c"]
numbers = [1, 2, 3, 4, 5]
combined = letters + numbers
print(combined)


# Creating a range list
numbers = list(range(20))
print(numbers)


# Creating a list that iterates over a string
word = list("Testing")
print(word)


# Finding highest value in a list
numbers = [1, 2, 3, 11, 5, 10]

highest_number = numbers[0]

for number in numbers:
    if number > highest_number:
        highest_number = number
print(highest_number)


# 2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix[0][2])

for row in matrix:
    for item in row:
        print(item)


# Lists
lst = [4, 2, 6, 1, 3, 5, 6]

# print(list[::-1])      # Returns items in reverse
# list.append(9)         # Append for adding items to the end of a list
# list.insert(1,9)       # Insert to insert value in the middle of a list
# list.remove(3)         # Remove to remove the first instance of specified value
# list.clear()           # Clear removes all items from list
# list.pop(1)            # Removes last item by default or item at index specified
# print(list.index(3))   # Gives index of item specified
# print(50 in list)      # Use in to check if item exists in list
# print(list.count(4))   # Count to check how many instances of an item in list
# list.sort()            # To sort list
# list.reverse()         # To reverse list
# list2 = list.copy()    # Copy creates a copy of your list
# del list[0:3]          # Delete a range of items

# Exercise to remove duplicates from list
uniques = []
for item in lst:
    if item not in uniques:
        uniques.append(item)

print(uniques)


# List unpacking
numbers = [1, 2, 3]
# The following:
one, two, three = numbers
# Is the same as:
one = numbers[0]
two = numbers[1]
three = numbers[2]
# You can also unpack lists to less variables and store the rest
numbers = [1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9]
one, two, *others = numbers
print(others)


# Get tuple of items in list
letters = ["a", "b", "c"]

for letter in enumerate(letters):
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)


# Finding index of item in list
letters = ["a", "b", "c", "a"]
print(letters.count("a"))
if "b" in letters:
    print(letters.index("b"))


# Sorting lists
numbers = [1, 3, 2, 53, 5, 12, 3]
# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))

# Sorting items in a dictionary
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


# Create function that returns the value to sort
def sort_item(item):
    return item[1]


# Use sort method and pass the function (sort_item) to give key
items.sort(key=sort_item)
print(items)

# Or to do this more cleanly, use a lambda function (an anonymous function)
items.sort(key=lambda item: item[1])
print(items)

# To get only the prices in the items array:
prices = list(map(lambda item: item[1], items))
print(prices)

# List comprehensions to do the map function mentioned above but cleaner
prices = [item[1] for item in items]

# To only get items where the value is >= 10
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# List comprehensions to do the map function mentioned above but cleaner
filtered = [item for item in items if item[1] >= 10]

# Zipping a list combines elements from multiple iterables
list1 = [1, 2, 3]
list2 = [100, 200, 300]
print(list(zip("abc", list1, list2)))

# Stacks - LIFO - last item added is removed first (e.g. browsing history)
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
browsing_session.pop()
print(browsing_session)
print(browsing_session[-1])
if not browsing_session:
    print("Clear browsing session, no items left in list")

# Queues - FIFO - using deque to access popleft function
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
print(list(queue))
length_of_queue = len(queue)
if not queue:
    print("Empty")
