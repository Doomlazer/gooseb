# gooseb
Minimalist reader for the Give Yourself Goosebumps gamebook series.

## The books

epub2gooseb.py is a python utility that converts the original 22 Give Yourself Goosebumps books
from epub format to the json file this reader uses. The epub files are not included with the 
project because you can buy them here: https://www.amazon.com/Give-Yourself-Goosebumps-41-book-series/dp/B07VXPL67N. Only the first 22 books are available out of 41. Let me know if you find the others.

Added epub2gooseb.py support for converting the Special Edition Epub of "trapped in the circus of fear".
It's a different epub format, but it seems to be a Scolastic version. You can download the .epub directly from
Archive.org <a href="https://archive.org/download/give-yourself-goosebumps-special-edition/Give%20Yourself%20Goosebumps%20Special%20Edition/03.Trapped%20in%20the%20Circus%20of%20Fear.epub">here</a>. 

### Convert epub to gooseb format

The following steps only need to be done once.

1) Place GYG epub files in 'books' folder.
2) `pip install EbookLib`
3) `pip install bs4`
4) `pip install py3-tts`
5) Change to gooseb folder.
6) `python3 epub2gooseb.py`

### Read the books with gooseb.py

7) `python3 gooseb.py`

## Special Editions

There are eight special edition books in the GYG series. They have additional game rules, such as 
dice roll events and Inventory items. The special edition book 'Into the Jaws of Doom' has been included
here as a preservation effort - the special editions didn't seem to recieve epub releases.

Note: the special edition epub files on archive.org are not compatible with epub2gooseb.py. They are 
epub versions of an OCR scan of the book - these versions have a lot of errors in the text and don't
share the same format as the Scholastic epubs.

Special edition features are still a work in progress. 

### Built in commands

Toggle the text-to-speech feature on and off with the in-game command: `tts`

To step backwards through the page history use: `prev` or `p`

To exit the program use: `quit`


## GOOSEB Reader JSON format

### Each book is required to have the following keys:

`banner` - the title of the book series. Printed at the top of each page.

`title` - title of the current book. Printed below the banner.

`length` - total number of numbered entries in the book (not including namedPages).

`namedPages` - required to access any non-numbered pages.

`help` - list of commands, named pages or other helpful info for the player.

`firstPage` - the page displayed after loading a book. Examples: 1, 230, "about", etc..

Non-numbered pages must be added to the 'namedPages' key to be accessable.
Example key: "namedPages":["intro","cover","instructions","help","about"],

### other keys:

Dice rolls can be added to the end of a page by creating a json key with
the format: pageNumber + "roll". 

Example: a key of "230roll" exisits in the file, it will add a dice roll the bottom
of page number 230. The value of the key is not currently read and can be anything.


