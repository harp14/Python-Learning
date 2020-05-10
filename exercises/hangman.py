# Hangman game
import random


def random_word_from_file():
    # Grab random word from dictionary file
    dictionary_file = open(
        # 'python_learning/exercises/hangman_dictionary.txt')
        'hangman_dictionary.txt')
    lines = dictionary_file.read().splitlines()
    return(random.choice(lines))


def play_game():
    # Create variables for game
    original_word = random_word_from_file()
    word_to_guess = original_word
    length_of_word = len(word_to_guess)
    number_of_guesses = 15

    print(f"Word is {length_of_word} letters long.")

    # While player still has guesses left
    while number_of_guesses > 0:
        user_input = input("Guess: ").lower()
        length_of_word = len(word_to_guess)

        # Continue while there are still letters left to guess
        if length_of_word > 1:

            # Ensure player only enters 1 letter at a time
            if len(user_input) == 1:

                # If player's guess is correct
                if user_input in word_to_guess:

                    # Remove letter guessed from word
                    word_to_guess = word_to_guess.replace(f'{user_input}', '')
                    length_of_word = len(word_to_guess)
                    print(
                        f"Well done! {length_of_word} letters left to guess!")
                else:
                    # If guess is incorrect
                    number_of_guesses -= 1
                    print(
                        f"Incorrect. You have {number_of_guesses} guesses left.")
            else:
                print("Only 1 letter allowed.")
                continue

        # If player has guessed all letters
        else:
            print("*" * 10)
            print(f"You won!!! The word was: {original_word}")
            print("*" * 10)
            main_menu()

    # If player runs out of guesses
    print("*" * 11)
    print("You lost!!!")
    print("*" * 11)


def main_menu():
    while True:
        # Main menu
        print("1. Play\n2. Quit")
        user_input = input("> ")
        if user_input == "1":
            play_game()
        elif user_input == "2":
            exit(0)
        else:
            print("Please enter a valid option")


main_menu()
