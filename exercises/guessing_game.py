import random


def play_game():
    random_number = random.randint(1, 10)
    guesses_left = 3
    print("*" * 35)
    print("Welcome to the guessing game!")
    print("Guess the number between 1 and 10!")
    print("*" * 35)

    while guesses_left > 0:
        user_guess = int(input("Number guessed: "))
        if user_guess == random_number:
            print("\n")
            print("*" * 35)
            print("*" * 35)
            print("*" * 12, "YOU WON!!", "*" * 12)
            print("*" * 35)
            print("*" * 35, "\n", "\n")
            menu_options()
        elif guesses_left > 1:
            guesses_left -= 1
            print(f"You have {guesses_left} guesses left")
            continue
        else:
            break

    print("\n")
    print("*" * 35)
    print("You ran out of guesses!")
    print("*" * 35, "\n")
    menu_options()


def menu_options():
    print("*" * 35)
    print("*" * 8, "The Guessing Game", "*" * 8)
    print("*" * 35)
    print("1. Play\n2. Quit")

    try:
        user_input = int(input("Enter selection: "))
    except ValueError:
        print("Please enter a valid option")
        menu_options()

    if user_input == 1:
        play_game()
    elif user_input == 2:
        exit(0)
    else:
        print("Please enter a valid option")
        menu_options()


menu_options()
