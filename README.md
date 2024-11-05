# gooseb
Minimalist reader for the Give Yourself Goosebumps gamebook series.

## Useage

epub2gooseb.py is a utility that will convert the original 22 Give Yourself Goosebumps books
from epub to the custom json format this reader uses. These files are not included with the 
project as Scholastic has issued copyright strikes against these files when hosted on archive.org.
Users must source the epub files themselves.

### Convert epub to gooseb format

The following steps only need to be done once.

1) Place GYG epub files in 'books' folder.
2) `pip install EbookLib`
3) `pip install bs4`
4) `pip install py3-tts`
5) Change to gooseb folder.
6) `python3 epub2gooseb.py`

### Run gooseb.py

7) `python3 gooseb.py`

The program should list any .json files in the 'books' folder of the user to load. This has been
tested with GYG books 1-22.

There are also special edition books in the GYG series with additional features, like dice rolls.
The special edition book 'Into the Jaws of Doom' has been included with the project files 
as the special editions did not recieve a copyright strike on archive.org from Scholastic. This file
may need to be removed (if requested by Scholatic), otherwise I will eventually add the other special edition
versions still avaialbe on archive.org eventually. 

Special edition features are still a work in progress.

### Built in commands

Toggle the text-to-speech feature on and off with the in-game command: `tts`

To step backwards thgough the page history use: `prev` or `p`

To exit the program use: `quit`


## GOOSEB Reader JSON format

The following is only relevant for users who want to edit or create their own gamebooks.

### Each book is required to have the following keys:

`banner` - the title of the book series. Printed at the top of each page.

`title` - title of the current book. Printed below the banner.

`length` - total number of numbered entries in the book (not including namedPages).

`namedPages` - required to access any non-numbered pages.

`help` - list of commands, named pages or other helpful info for the player.

`firstPage` - the page displayed after loading a book. Examples: 1, 230, "about", etc..

Non-numbered pages must be added to the 'namedPages' key to be accessable.
Example key: "namedPages":["intro","cover","instructions","help","about"],

### Additionl keys:

Dice rolls can be added to the end of a page by creating a json key with
the format: pageNumber + "roll". 

Example: a key of "230roll" exisits in the file, it will add a dice roll the bottom
of page number 230. The value of the key is not currently read and can be anything.
