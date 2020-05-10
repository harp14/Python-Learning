# If else statements
temperature = "Brr"

if temperature == 'Hot':
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature == "Cold":
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


# If else boolean statements
has_good_credit = True
has_criminal_record = False


if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# If else name validation
name = input("Enter your name: ")

if len(name) < 3:
    print("Name must be more than 3 characters long")
elif len(name) > 50:
    print("Name must be less than 50 characters long")
else:
    print("Name looks good!")
