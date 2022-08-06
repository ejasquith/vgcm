"""
Creates SheetConnection object to handle connection
to Google Sheets using gspread
Classes:
    SheetConnection
"""

import gspread
from google.oauth2.service_account import Credentials


class SheetConnection():
    """
    Class used to handle connection to Google Sheet API
    Should never be instantiated directly; use SheetConnection.get_instance()

    Attributes:
        instance : SheetConnection
    Methods:
        get_instance
        insert_record
        get_all_records
        overwrite_records
    """
    instance = None

    def __init__(self):
        SheetConnection.instance = self

        self._SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

        self._CREDS = Credentials.from_service_account_file("creds.json")
        self._SCOPED_CREDS = self._CREDS.with_scopes(self._SCOPE)

        self._GSPREAD_CLIENT = gspread.authorize(self._SCOPED_CREDS)

        self._SHEET = self._GSPREAD_CLIENT.open("vgcm_data")

    @staticmethod
    def get_instance():
        """
        Returns the running instance of SheetConnection,
        or creates a new one if none exists
        """
        if SheetConnection.instance is None:
            SheetConnection.instance = SheetConnection()
        return SheetConnection.instance

    def insert_record(self, game):
        """
        Inserts a game object into Google Sheet
        """
        values = game.listify()
        games_sheet = self._SHEET.worksheet("games")
        games_sheet.append_row(values)

    def get_all_records(self):
        """
        Returns all records as a list of lists
        """
        return self._SHEET.worksheet("games").get_all_values()

    def overwrite_records(self, records):
        """
        Overwrites sheet with a list of games
        """
        self._SHEET.worksheet("games").clear()
        for record in records:
            self.insert_record(record)
