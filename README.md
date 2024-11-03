# gooseb
Minimalist reader for the Give Yourself Goosebumps gamebook series

Useage: python3 gooseb.py

Add gamebooks in JSON format to the 'books' folder. Currently, I've only
formatted one book for use with this reader, but more can be added.


### Reader JSON format

Each book is required to have the following keys in the json file:

banner - the title of the book series. Printed at the top of each page.
title - title of the current book. Printed below the banner.
length - total number of numbered entries in the book (not including namedPages).
namedPages - required to access any non-numbered pages.
help - list of commands, named pages or other helpful info for the player.
firstPage - the page displayed after loading a book. Examples: 1, 230, "about", etc..

Named pages must be added to the 'namedPages' key to be accessable.
Example key: "namedPages":["intro","cover","instructions","help","about"],

Addiionl keys:

Dice rolls can be added to the end of a page by creating a json key with
the format: pageNumber + "roll". 

Example: a key of "230roll" exisits in the file, it will add a dice roll the bottom
of page number 230. The value of the key is not currently read and can be anything.