"""
Handle connection to PostrgreSQL database.

Methods:
    create_game
    delete_game
    find_game
    get_all_games
"""

from game import Game
from datetime import datetime

# Connect to DB
# Using Python data structures during development

records = [
    Game("Fallout: New Vegas", "RPG", "Bethesda Softworks",
         "Obsidian Entertainment", "Xbox 360",
         datetime(2010, 10, 22), datetime(2022, 6, 3)),
    Game("The Outer Worlds", "RPG", "Private Division",
         "Obsidian Entertainment", "PC",
         datetime(2019, 10, 25), datetime(2022, 7, 17)),
    Game("Sonic the Hedgehog", "Platformer", "Sega",
         "Sonic Team", "Sega Genesis",
         datetime(1991, 6, 23), datetime(2012, 4, 18))
]


def create_game(title, genre, publisher, developer,
                platform, release_date, purchase_date):
    """
    Creates game object with given parameters and inserts into database
    """
    pass


def delete_game(title, genre, publisher, developer,
                platform, release_date, purchase_date):
    """
    Finds and deletes game with given parameters.
    If no game exists, returns None
    """
    pass


def find_game(**kwargs):
    """
    Returns game objects that match given parameters.
    Parameters are optional but at least one must be given

    Accepted parameters:
        title : str
        genre : str
        publisher : str
        developer : str
        platform : str
    """
    pass


def get_all_games():
    """
    Returns a list of all game objects in database.
    """
    return records
