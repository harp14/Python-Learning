# While loop countdown
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print('We have blast off!')


# While loops
i = 1;
while i <= 5:
    print('*' * i)
    i += 1


# Guessing game
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('You ran out of guesses!')


# Car game
command = ''
car_started = False

while True:
    command = input('>').lower()
    if command == 'start':
        if car_started:
            print("Car is already started")
        else:
            car_started = True
            print("Car started...Ready to go!")
    elif command == 'stop':
        if car_started:
            car_started = False
            print("Car stopped.")
        else:
            print("Car hasn't been started")
    elif command == 'help':
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to quit")
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that")