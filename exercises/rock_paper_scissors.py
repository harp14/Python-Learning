import random


def get_item(item_number):
    items = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors",
        "4": "Lizard",
        "5": "Spock"
    }
    return items.get(f"{item_number}")


def play_game():
    while True:
        computer_selected_option = ''
        user_selected_option = ''
        computer_selection_number = random.randint(1, 5)
        computer_selected_option = get_item(computer_selection_number)

        print("*" * 30)
        print("1. Rock\n2. Paper\n3. Scissors\n4. Lizard\n5. Spock")
        user_selection_number = int(input("Enter selection: "))
        user_selected_option = get_item(user_selection_number)
        print("*" * 30)
        print(f"Computer selected: {computer_selected_option}")

        if user_selected_option == "Rock":
            if computer_selected_option == "Rock":
                print(f"A tie! Try again!")
                continue
            elif computer_selected_option == "Paper":
                print("You lost! Computer selected paper!")
                exit(0)
            elif computer_selected_option == "Lizard":
                print("You squashed the lizard! You won!")
                exit(0)
        elif user_selected_option == "Paper":
            if computer_selected_option == "Paper":
                print(f"A tie! Try again!")
                continue
            elif computer_selected_option == "Rock":
                print("You won! Computer selected rock!")
                exit(0)


def menu_options():
    print('1. Play\n2. Quit')

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
