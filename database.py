"""
Create database object to handle operations

Classes:
    Database
"""

from copy import copy
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

    def __init__(self, file=None):
        if file is not None:
            # Parse file and load
            self.load_file(file)
        else:
            self._records = []

    def create_game(self, **kwargs):
        """
        Creates game object with given parameters and inserts into database
        """
        self._records.append(
            Game(kwargs["title"], kwargs["genre"], kwargs["publisher"],
                 kwargs["developer"], kwargs["platform"],
                 kwargs["release_date"], kwargs["purchase_date"])
        )

    def delete_games(self, **kwargs):
        """
        Finds and deletes games with given parameters.
        If no game exists, returns None
        """
        games = self.find_games(**kwargs)
        self._records = [game for game in self._records if game not in games]

    def find_games(self, **kwargs):
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
        searched_list = copy(self._records)
        for key, value in kwargs.items():
            searched_list = [record for record in searched_list
                             if getattr(record, key) == value]
        return searched_list

    def get_all_games(self):
        """
        Returns a list of all game objects in database.
        """
        return self._records

    def load_file(self, file_name):
        """
        Loads _records attribute from json file
        """
        pass

    def save_file(self, file_name):
        """
        Saves records to json file
        """
        pass
