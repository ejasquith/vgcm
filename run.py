from tabulate import tabulate
import database

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


def main():
    print(LOGO)
    print(WELCOME_MESSAGE)
                            
    while (user_input := input(MENU)) != "5":
        if user_input == "1":
            # Add game
            pass
        elif user_input == "2":
            # Display games
            pass
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
