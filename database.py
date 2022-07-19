"""
Handle connection to PostrgreSQL database.

Methods:
    create_game
    delete_game
    find_game
    get_all_games
"""

# Connect to DB
# Using Python data structures during development

records = []


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


def find_game(title, genre, publisher, developer,
              platform, release_date, purchase_date):
    """
    Returns game objects that match given parameters in a list.
    Parameters are optional but at least one must be given
    """
    pass


def get_all_games():
    """
    Returns a list of all game objects in database.
    """
    pass
