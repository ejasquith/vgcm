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

run.py contains all the code used to execute the application in a command line interface.

game.py contains the logic used to digitally represent games in memory, using a class.

database.py contains the code to manage in-memory data storage.

Finally, sheetconnection.py contains the code used to connect to Google Sheets.

The codebase was designed in this way so that parts of the system could be slotted in and out with relative ease - if a GUI were to be developed, it could continue to use the game, database and sheetconnection files. Similarly, if it was decided to use a database such as PostgreSQL to persistently store data, the sheetconnection class could be replaced.

# Features

VGCM offers a way to manage and store information on a collection of video games through a command line interface.

## Welcome Message

Upon loading the application, the user is presented with an ASCII art style logo, and a welcome message. This is primarily intended to subconsciously let the user know that the program has loaded correctly, while also displaying the name and purpose of the software. There is also a pause in execution while the Google Sheet is loaded, so I included a status message saying "loading database" to reassure the user that the program has not crashed.

![An image of the welcome message](docs/images/welcome.png)

## Menu

After the welcome message has been displayed, a menu is output to the user with a list of functions. The user must enter the number corresponding to the option they want to choose.

![An image of the menu](docs/images/menu.png)

If an invalid input is entered, the program displays an error message and the menu is displayed again.

 ![An image of the menu after a user inputs an invalid choice](docs/images/invalid-menu-input.png)

 ## Display All Games

 The first option in the menu is to display all games. On selecting this, another menu is displayed asking the user what attribute to sort the list by - they can choose any of the attributes on the games (title, genre, publisher, platform, release date), or leave blank to leave the list in its default order. This menu has similar input validation to the main menu.

 The list of games is then displayed in a table format, and the user is again prompted to enter a main menu choice.

 ![An image of the menu displayed after selecting display all games](docs/images/display-all-menu.png)

 ![An image of the table of results for displaying all games, sorted by title](docs/images/display-all-results.png)

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

# Deployment

In order to run backend Python code, the app has been deployed to [Heroku](https://www.heroku.com). There are a number of steps to do this:

- From your workspace, run the command `pip freeze > requirements.txt`
- Create a Heroku account and create a new app.
- Under the settings tab, add the config vars:
    - `PORT: 8000`
    - `CREDS:`
        - Here, copy in the contents of creds.json that allow you to connect to Google Sheets.
- Under buildpacks in the settings tab, add Python and Node.js.
- Under the deploy tab, connect to your GitHub account and select the repository to connect to.
- Under manual deploy, select branch main and click deploy.

# Credits

