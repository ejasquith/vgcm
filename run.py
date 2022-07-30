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


def prompt_string_input(prompt, allow_empty):
    """
    Prompts user to enter a non-empty string
    Returns valid input
    """
    valid = False
    while not valid:
        user_input = input(prompt)
        if user_input or allow_empty:
            valid = True
        else:
            print("String must not be empty. Please try again.")
    return user_input


def prompt_date_input(prompt, allow_empty):
    """
    Prompts user to enter a date
    Returns datetime object from valid input
    """
    valid = False
    while not valid:
        try:
            date = datetime.strptime(input(prompt), "%d/%m/%Y")
        except ValueError:
            if allow_empty:
                return ""
            else:
                print("Date in invalid format. Should be in format DD/MM/YYYY")
                print("Please try again.")
        else:
            valid = True
    return date


def prompt_game_details_input(allow_empty):
    """
    Prompts user to enter details for new Game object
    Returns dict of inputted values
    """
    values = {}

    print("\nEnter game details:")
    values["title"] = prompt_string_input("Title: ", allow_empty)
    values["genre"] = prompt_string_input("Genre: ", allow_empty)
    values["publisher"] = prompt_string_input("Publisher: ", allow_empty)
    values["developer"] = prompt_string_input("Developer: ", allow_empty)
    values["platform"] = prompt_string_input("Platform: ", allow_empty)
    values["release_date"] = prompt_date_input("Release date: ", allow_empty)
    values["purchase_date"] = prompt_date_input("Purchase date: ", allow_empty)

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
            values = prompt_game_details_input(False)
            database.create_game(**values)
        elif user_input == "2":
            # Display games
            print("\n"+format_table_output(database.get_all_games()))
        elif user_input == "3":
            # Search games
            print("Enter details or leave blank to skip field")
            values = prompt_game_details_input(True)
            games = database.find_game(**values)
            print("\n"+format_table_output(games))
        elif user_input == "4":
            # Remove game
            print("Enter details of game(s) to delete, or leave blank to skip field")
            values = prompt_game_details_input(True)
            games = database.find_game(**values)
            
            if games:
                print("\n"+format_table_output(games))
                print("Are you sure you want to delete these games? (y/n)")
                while (choice := input("> ").lower()) not in ("n", "no"):
                    if choice in ("y", "yes"):
                        try:
                            database.delete_game(**values)
                        except Exception as exc:
                            print("Error: ", exc.args)
                        else:
                            print("Games successfully deleted.")
                        finally:
                            break
                    else:
                        print("Please enter y or n.")
            else:
                print("\nNo games found.")

        else:
            # Invalid input
            print("Invalid input. Please enter a number 1-5")


main()
