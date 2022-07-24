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


def check_valid_date(string):
    """
    Checks if a string is a valid date in format DD/MM/YYYY.
    Raises ValueError if invalid
    Returns datetime object from original string
    """
    try:
        date = datetime.strptime(string, "%d/%m/%Y")
    except ValueError as verr:
        # Raises an exception with custom message
        # from keyword indicates direct cause
        raise ValueError(
            "Date in invalid format. Should be in format DD/MM/YYYY"
        ) from verr
    else:
        return date


def check_valid_string(string):
    """
    Checks if a string is empty
    Raises ValueError if empty
    Returns original string
    """
    # Empty strings are falsy
    if not string:
        raise ValueError("String cannot be empty.")
    else:
        return string


def prompt_game_details_input():
    """
    Prompts user to enter details for new Game object
    Returns list of inputted values
    """
    valid = False

    while not valid:
        values = []
        print("Enter game details:")
        try:
            values.append(check_valid_string(input("Title: ")))
            values.append(check_valid_string(input("Genre: ")))
            values.append(check_valid_string(input("Publisher: ")))
            values.append(check_valid_string(input("Developer: ")))
            values.append(check_valid_string(input("Platform: ")))
            values.append(check_valid_date(input("Release date: ")))
            values.append(check_valid_date(input("Purchase date: ")))

            valid = True
        except ValueError as verr:
            print(f"Invalid input: {verr}")
            print("Please try again.")

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
            values = prompt_game_details_input()
            database.create_game(values)
        elif user_input == "2":
            # Display games
            print("\n"+format_table_output(database.get_all_games()))
        elif user_input == "3":
            # Search games
            pass
        elif user_input == "4":
            # Remove game
            pass
        else:
            # Invalid input
            pass


main()
