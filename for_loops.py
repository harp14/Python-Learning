# For loop in list
for number in [2, 4, 6, 8]:
    print(number)
print('Who do we appreciate?')


# For loop in range
for x in range(10):
    print(x * x)


# For loops
for letter in 'Python':
    print(letter)

for item in [1, 2, 3, 4]:
    print(item)

for item in range(5, 10, 2):
    print(item + 1)

prices = [10, 20, 30]

total = 0

for price in prices:
    total += price

print(total)

# Nested for loops
for x in range(4):
    for y in range(4):
        print(f'{x},{y}')

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# Print number of even numbers in a range
number_of_evens = 0

for number in range(1, 10):
    if number % 2 == 0:
        number_of_evens += 1
        print(number)

print(f"We have {number_of_evens} even numbers")
