number_to_divide = int(input("Enter a number to divide: "))
divide_by = int(input("Enter number to divide by: "))

if (number_to_divide % divide_by == 0):
    print("Number is divisible")
else:
    print("Number is not divisible")

# Check if number is odd or even
number = int(input("Enter a number: "))

if (number % 4 == 0):
    print("Number is divisible by 4")
elif (number % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")
