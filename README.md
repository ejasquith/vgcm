# VGCM - Video Game Collection Manager

The aim of this project is to provide a simple application for a video game collector to manage their collection.  

# Planning Stage

## User Stories

- As a user, I want to add games to my collection
- As a user, I want to remove games from my collection
- As a user, I want to view my collection
- As a user, I want to search and sort my collection
- As a user, I want to save and load my collection

## Categories

In order to sort the collection, each game must have a number of categories that it can be searched by.  

These will include:
- Title (eg. Fallout: New Vegas)
- Genre (eg. RPG)
- Publisher (eg. Bethesda Softworks)
- Developer (eg. Obsidian Entertainment)
- Platform (eg. Xbox 360)
- Release Date (eg. 22/10/2010)
- Purchase Date (eg. 03/06/2022)

During development, the developer and purchase date attributes had to be scrapped due to the 80 character width of the virtual terminal the project would be hosted on. This was to ensure all data is correctly presented to the user.

# Development Stage

## Code Architecture

The code for this project is designed to be as reusable as possible. It is separated into four distinct python files (run.py, game.py, database.py and sheetconnection.py).

run.py contains all the code used to execute the application in a command line interface. This can be considered the view in model-view-controller architecture.

game.py contains the logic used to digitally represent games in memory, using a class. This is the model.

database.py contains the code to manage in-memory data storage. This is the controller.

Finally, sheetconnection.py contains the code used to connect to Google Sheets.

The codebase was designed in this way so that parts of the system could be slotted in and out with relative ease - if a GUI were to be developed, it could continue to use the game, database and sheetconnection files. Similarly, if it was decided to use a database such as PostgreSQL to persistently store data, the sheetconnection class could be replaced.

# Testing

## Bugs

- When implementing input validation for creating a new game, an error would be thrown when one of the initially entered values was invalid, even if the final inputs were valid.
    - This was because the list the values were being appended to had been declared outside the while loop, meaning the previous values were still in the list.
    - That list was then being passed to the database to create a new game, which included more values than expected, causing the error.
- When deleting games, none would be deleted even though the correct games were found.
    - This was because the `delete_game` function called `find_game`, which used a deep copy of the database's records.
        - This meant that the object references were not the same as the originals, meaning comparing an object's id from the `find_game` function and the "same" object from the original records would return false.
        - Subsequently, the `delete_game` function didn't find any objects in the original records that matched the ones it was asked to delete.
    - Changing find_game to create a shallow copy fixed this issue.
- When the `prompt_date_input` function was called passing `allow_empty=True`, an invalid date would be accepted as a valid input.
    - This was due to the try block catching the exception when parsing the string, but there was only a single condition checking whether `allow_empty` was true to determine if the input should actually be accepted.
    - I changed the condition to `if not user_input and allow_empty`, which only evaluates to true if the input string is empty.

# Credits

