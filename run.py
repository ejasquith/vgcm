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


def main():
    print(LOGO)
    print(WELCOME_MESSAGE)
    print(tabulate(database.get_all_games()))


main()
