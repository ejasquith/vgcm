"""
Create database object to handle operations

Classes:
    Database
"""

from datetime import datetime
from game import Game


class Database:
    """
    A class used to handle database operations.

    Attributes:
        _records : list
    Methods:
        create_game
        delete_game
        find_game
        get_all_games
        load_file
        save_file
    """

    def __init__(self, file):
        if file is not None:
            # Parse file and load
            self.load_file(file)
        else:
            self._records = []

    def create_game(self, title, genre, publisher, developer,
                    platform, release_date, purchase_date):
        """
        Creates game object with given parameters and inserts into database
        """
        self._records.append(
            Game(title, genre, publisher, developer,
                 platform, release_date, purchase_date)
        )

    def delete_game(self, title, genre, publisher, developer,
                    platform, release_date, purchase_date):
        """
        Finds and deletes game with given parameters.
        If no game exists, returns None
        """
        pass

    def find_game(self, **kwargs):
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

    def get_all_games(self):
        """
        Returns a list of all game objects in database.
        """
        return self._records

    def load_file(self, file):
        """
        Loads _records attribute from csv file
        """
        pass

    def save_file(self, file_name):
        """
        Saves records to csv file
        """
        pass
