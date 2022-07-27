from datetime import datetime
from tabulate import tabulate
from database import Database

LOGO = """
 _    ________________  ___
| |  / / ____/ ____/  |/  /
| | / / / __/ /   / /|_/ /
| |/ / /_/ / /___/ /  / /
|___/\____/\____/_/  /_/

"""

WELCOME_MESSAGE = "Welcome to VGCM - Video Game Collection Manager"

MENU = """
1) Add a game to your collection
2) Display all games in your collection
3) Search for a game in your collection
4) Remove a game from your collection
5) Exit
> """


def format_table_output(games):
    """
    Formats a list of games into a table
    """
    games_properties = [game.listify() for game in games]
    return tabulate(games_properties,
                    headers=["Title", "Genre", "Publisher", "Developer",
                             "Platform", "Release Date", "Purchase Date"])


def prompt_string_input(prompt):
    """
    Prompts user to enter a non-empty string
    Returns valid input
    """
    valid = False
    while not valid:
        user_input = input(prompt)
        if user_input:
            valid = True
        else:
            print("String must not be empty. Please try again.")
    return user_input


def prompt_date_input(prompt):
    """
    Prompts user to enter a date
    Returns datetime object from valid input
    """
    valid = False
    while not valid:
        try:
            date = datetime.strptime(input(prompt), "%d/%m/%Y")
        except ValueError:
            print("Date in invalid format. Should be in format DD/MM/YYYY")
            print("Please try again.")
        else:
            valid = True
    return date


def prompt_game_details_input():
    """
    Prompts user to enter details for new Game object
    Returns list of inputted values
    """
    values = []

    print("\nEnter game details:")
    values.append(prompt_string_input("Title: "))
    values.append(prompt_string_input("Genre: "))
    values.append(prompt_string_input("Publisher: "))
    values.append(prompt_string_input("Developer: "))
    values.append(prompt_string_input("Platform: "))
    values.append(prompt_date_input("Release date: "))
    values.append(prompt_date_input("Purchase date: "))

    return values


def main():
    """
    Main program loop
    """
    print(LOGO)
    print(WELCOME_MESSAGE)

    database = Database()

    while (user_input := input(MENU)) != "5":
        if user_input == "1":
            # Create new game
            values = prompt_game_details_input()
            database.create_game(values)
        elif user_input == "2":
            # Display games
            print("\n"+format_table_output(database.get_all_games()))
        elif user_input == "3":
            # Search games
            print("Enter game title:")
            games = database.find_game(title=input("> "))
            print("\n"+format_table_output(games))
        elif user_input == "4":
            # Remove game
            pass
        else:
            # Invalid input
            print("Invalid input. Please enter a number 1-5")


main()
