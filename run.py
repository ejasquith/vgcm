"""
Main program file.

Methods:
    format_table_output
    prompt_string_input
    prompt_date_input
    prompt_sort_attribute
    prompt_game_details_input
    sort_games
    main
"""

import sys
from datetime import datetime
from tabulate import tabulate
from gspread import GSpreadException
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

SORT_MENU = """
Choose attribute to sort list by, or leave empty to keep default order:
1) Title
2) Genre
3) Publisher
4) Platform
5) Release date"""


def format_table_output(games):
    """
    Formats a list of games into a table
    """
    games_properties = [game.listify() for game in games]
    return tabulate(
        games_properties,
        headers=["Title", "Genre", "Publisher", "Platform", "Release Date"],
        maxcolwidths=12,
        tablefmt="grid",
    )


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
        user_input = input(prompt)
        try:
            date = datetime.strptime(user_input, "%d/%m/%Y")
        except ValueError:
            if not user_input and allow_empty:
                return ""
            else:
                print("Date in invalid format. Should be in format DD/MM/YYYY")
                print("Please try again.")
        else:
            valid = True
    return date


def prompt_sort_attribute():
    """
    Prompts user to enter attribute to sort list of games by
    """
    valid = False
    while not valid:
        print(SORT_MENU)
        user_input = input("> ")
        if not user_input:
            return None
        elif user_input in ["1", "2", "3", "4", "5"]:
            return int(user_input)
        else:
            print("Invalid input. Please enter 1-5 or leave blank.")


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
    values["platform"] = prompt_string_input("Platform: ", allow_empty)
    values["release_date"] = prompt_date_input("Release date: ", allow_empty)

    return values


def sort_games(games, sort_attr):
    """
    Sorts a list of games based on user input from prompt_sort_attribute
    """
    if sort_attr == 1:
        games.sort(key=lambda game: game.title)
    elif sort_attr == 2:
        games.sort(key=lambda game: game.genre)
    elif sort_attr == 3:
        games.sort(key=lambda game: game.publisher)
    elif sort_attr == 4:
        games.sort(key=lambda game: game.platform)
    elif sort_attr == 5:
        games.sort(key=lambda game: game.release_date)

    return games


def main():
    """
    Main program loop
    """
    print(LOGO)
    print(WELCOME_MESSAGE)

    print("\nLoading database...")
    try:
        database = Database()
    except GSpreadException:
        print("There was an error connecting to Google Sheets.")
        print("Exiting.")
        sys.exit(1)

    while (user_input := input(MENU)) != "5":
        if user_input == "1":
            # Create new game
            values = prompt_game_details_input(False)
            print("\nSaving game...")
            try:
                database.create_game(**values)
            except GSpreadException:
                print("There was an error connecting to Google Sheets.")
            else:
                print(f"{values['title']} successfully saved.")

        elif user_input == "2":
            # Display games
            games = database.get_all_games()
            sort_attr = prompt_sort_attribute()
            sort_games(games, sort_attr)
            print("\n" + format_table_output(games))

        elif user_input == "3":
            # Search games
            print("Enter details or leave blank to skip field")
            values = prompt_game_details_input(True)
            # Remove entries with empty values
            values = {key: value for key, value in values.items() if value}
            games = database.find_games(**values)
            if games:
                sort_attr = prompt_sort_attribute()
                sort_games(games, sort_attr)
                print("\n" + format_table_output(games))
            else:
                print("\nNo games found.")

        elif user_input == "4":
            # Remove game
            print("Enter details of game(s) to delete,",
                  "or leave blank to skip field")
            values = prompt_game_details_input(True)
            # Remove entries with empty values
            values = {key: value for key, value in values.items() if value}
            games = database.find_games(**values)

            if games:
                print("\n" + format_table_output(games))
                print("\nAre you sure you want to delete these games? (y/n)")
                while (choice := input("> ").lower()) not in ("n", "no"):
                    if choice in ("y", "yes"):
                        print("\nDeleting games...")
                        try:
                            database.delete_games(**values)
                        except GSpreadException:
                            print("There was an error",
                                  "connecting to Google Sheets.")
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


if __name__ == "__main__":
    main()
