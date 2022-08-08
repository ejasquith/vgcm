"""
Create database object to handle operations

Classes:
    Database
"""

from datetime import datetime
from copy import copy
from game import Game
from sheetconnection import SheetConnection


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
        load_sheet
    """

    def __init__(self):
        self._records = []
        # Parse file and load
        self.load_sheet()

    def create_game(self, **kwargs):
        """
        Creates game object with given parameters and inserts into database
        """
        game = Game(
            kwargs["title"],
            kwargs["genre"],
            kwargs["publisher"],
            kwargs["platform"],
            kwargs["release_date"],
        )
        self._records.append(game)
        SheetConnection.get_instance().insert_record(game)

    def delete_games(self, **kwargs):
        """
        Finds and deletes games with given parameters.
        If no game exists, returns None
        """
        games = self.find_games(**kwargs)
        self._records = [game for game in self._records if game not in games]
        SheetConnection.get_instance().overwrite_records(self._records)

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
        # Make a copy of original, which will have 
        # non-matching records removed
        searched_list = copy(self._records)
        for key, value in kwargs.items():
            # Have to iterate through original
            # Because removing records from a list while iterating
            # Causes weird problems
            for record in self._records:
                if str(value).lower() not in str(getattr(record, key)).lower():
                    searched_list.remove(record)
        return searched_list

    def get_all_games(self):
        """
        Returns a list of all game objects in database.
        """
        return self._records

    def load_sheet(self):
        """
        Loads _records attribute from Google Sheet
        """
        records = SheetConnection.get_instance().get_all_records()
        for record in records:
            title = record[0]
            genre = record[1]
            publisher = record[2]
            platform = record[3]
            release_date = datetime.strptime(record[4], "%d/%m/%Y")
            self._records.append(Game(title, genre, publisher,
                                      platform, release_date))
