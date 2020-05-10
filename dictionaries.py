'''
# Dictionaries
customer = {
    # The keys below need to be unique
    "name": "Harry",
    "age": 30,
    "is_verified": True
}

# If dictionary key birthday doesn't exist, return default value specified below
print(customer.get("address","44 Brynhyfryd Avenue"))

# Change key value as below
customer["name"] = "Harpreet"

# Create new key value pair as below
customer["birthday"] = "23rd April 1991"

print(customer)

# Dictionary to convert number to text
user_input = input('Number: ')

numbers = {
    "0": "Zero ",
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four ",
    "5": "Five ",
    "6": "Six ",
    "7": "Seven ",
    "8": "Eight ",
    "9": "Nine "
}

answer = ""

for digits in user_input:
    answer += numbers.get(digits,"!") + " "

print(answer)


# Emoji Converter
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😟",
    }

    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output

message = input('>')
print(emoji_converter(message))

'''

# Can create a dictionary using key value pairs as shown below using curly brackets
point = {"x": 1, "y": 2}

# Can also use the dict() function to create a dictionary as shown below:
point = dict(x=1, y=2)

# Get value of x as shown below (note the use of double quotes when string index)
print(point["x"])

# Can change the value against an index as shown below
point["x"] = 10

# Add a new key as shown below
point["z"] = 20

# Can check for the existance of a key in a dictionary to prevent key error
if "a" in point:
    print(point["a"])

# Or use the get method to return none/or custom return value if key doesn't exist
print(point.get("a", 0))

# Can delete value using key as shown below
#del point["x"]

# How to loop over dictionary
for key in point:
    print(key, point[key])

# Or use items method to get values
for key, value in point.items():
    print(key, value)

# Example of program using dictionaries
directory = {}

print("Welcome to the phone directory")


def menu():
    print("1. View all records\n2. Add a new record\n3. Delete a record\n4. Exit")
    user_choice = int(input("> "))

    while True:
        if user_choice == 1:
            print(directory)
            menu()
        elif user_choice == 2:
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            directory[name] = phone_number
            print("Record added!")
            menu()
        elif user_choice == 3:
            print("Which record would you like to delete?")
            to_delete = input("> ")
            if to_delete in directory:
                directory.pop(to_delete)
                print(f"Record for {to_delete} deleted")
            else:
                print("Record does not exist")
            menu()
        elif user_choice == 4:
            print("Goodbye!")
            exit(0)
        else:
            print("Enter a valid option")
            menu()
