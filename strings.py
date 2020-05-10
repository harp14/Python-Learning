# Multi-line strings
email_text = """
Dear Harry,

This is a test email spanning multiple lines.

Thanks,
Harry
"""
print(email_text)


# String methods - functions that belong to/are specific to an object are called methods
course = "Python for Beginners"
print(course.title())
print(course.upper())
print(course.lower())
print(course.find('Beg'))
print(course.replace('Beginners', 'Losers'))
print('Python' in course)


# Getting length of a string
example_string = "This is a string"
string_length = len(example_string)
print(string_length)


# Getting string characters from an index
test_string = 'This is a test string'
print(test_string[2:6])
# Gets string characters from the end
print(test_string[-3:-1])


# Formatted strings
first_name = "Harry"
last_name = "Matharu"
# Normal string version below
message = first_name + ' [' + last_name + '] is a coder'
# Formatted string version below
msg = f'{first_name} [{last_name}] is a coder'
print(message)
print(msg)


# Escape characters
print("This is a test of printing \" in the middle of a string")
print("This is a test of printing \' in the middle of a string")
print("This is a test of printing \\ in the middle of a string")
print("This is a test of printing \n in the middle of a string")
