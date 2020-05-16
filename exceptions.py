# Handling exceptions prevents your program from crashing and allows it to continue
try:
    # Closing a file when opening it in the following way only works for certain types of resources
    file = open("app.py")

    # The proper way to deal with resources you want to release automatically is as below
    # with open("app.py") as file:

    # If you want to work with multiple files do the following:
    with open("app.py") as file, open("another.txt") as target:
        # Here you can work with the file before it is automatically closed
        # This method doesn't require the finally clause below
        print("File opened")

    age = int(input("Age: "))
    xfactor = 10 / age
# Can set an exception error for multiple types of exceptions
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions thrown")
# The finally clause is always ran - regardless of errors, handy for things such as releasing resources
finally:
    file.close()


# Raising exceptions - causing an exception to be thrown on purpose
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


# If you do not run the function above with a try block you won't get
# only the error message
try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
