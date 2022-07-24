"""
Create database object to handle operations

Classes:
    Database
"""

import json
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

    def __init__(self, file=None):
        if file is not None:
            # Parse file and load
            self.load_file(file)
        else:
            self._records = []

    def create_game(self, attr_list):
        """
        Creates game object with given parameters and inserts into database
        """
        title, genre, publisher, developer, platform, release_date, purchase_date = attr_list
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

    def load_file(self, file_name):
        """
        Loads _records attribute from json file
        """
        self._records = []

        try:
            file = open(f"{file_name}.json", "r")
        except IOError as error:
            print(error.strerror)
            return

        try:
            for record in file:
                json_dict = json.loads(record)
                game = Game(json_dict.title, json_dict.genre, json_dict.publisher,
                            json_dict.developer, json_dict.platform,
                            datetime(json_dict.release_date), datetime(json_dict.purchase_date))
                self._records.append(game)
        except Exception:
            print("Data not in correct format. Please check the file you are trying to load.")
        finally:
            file.close()

    def save_file(self, file_name):
        """
        Saves records to json file
        """
        file = open(f"{file_name}.json", "x")
        for record in self._records:
            file.write(
                # Code from user12642493 on StackOverflow to
                # serialize object with datetime attribute
                # https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
                json.dumps(record, default=lambda o:
                           o.isoformat() if (isinstance(o, datetime)) else o.__dict__,
                           sort_keys=True, indent=4)
            )
        file.close()
