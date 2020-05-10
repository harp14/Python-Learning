# Print length of text
print(len('Hello World!'))


# Taking input
name = input('What is your name?: ')
print('Hello ' + name + ', your name is ' + str(len(name)) + ' characters long!')


# Checking user input length
userInput = input('Please enter a four-letter word: ')
if len(userInput) == 4:
    print(userInput + ' is a four letter word!')
else:
    print(userInput + ' is not a four letter word!')