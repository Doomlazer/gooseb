
import os
import json
# pip install bs4
from bs4 import BeautifulSoup
# pip install EbookLib
import ebooklib
from ebooklib import epub
# ebooklib produces annoying warnings, suppress them
import warnings
warnings.filterwarnings(action='ignore', category=FutureWarning)
warnings.filterwarnings(action='ignore', category=UserWarning)

def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    # remove leading " "
    text.pop(0)
    return '\n\n'.join(text) + '\n'

def convert(f):
    print("converting: " + f)
    book = epub.read_epub("./books/"+f)
    #creator = book.get_metadata('DC', 'creator')[0]
    title = book.get_metadata('DC', 'title')[0][0]
    description = book.get_metadata('DC', 'description')[0][0]
    namedPages = ["help","description"]
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

    # get chapters from ePub
    chapters = []
    for i in items:
        if '_ch' in i.get_name():
            chapters.append(i)

    # use module to parse html
    entries = []
    for c in chapters:
        entries.append(chapter_to_str(c))

    # pack required keys and text
    fileData = {}
    fileData['banner'] = "R.L. Stine's Give Yourself Goosebumps"
    fileData['title'] = str(title)
    fileData['length'] = len(chapters)
    fileData['namedPages'] = namedPages
    fileData['help'] = "Commands: description, prev, quit"
    fileData['firstPage'] = 1
    fileData['description'] = description
    for x in range(len(entries)):
        fileData[x+1] = str(entries[x])

    json_object = json.dumps(fileData, indent=4)

    # Write json file
    b = f.split('.')
    with open("./books/" + b[0] + ".json", "w") as outfile:
        outfile.write(json_object)


def run():
    dirList = os.listdir("./books")
    for l in dirList:
        # filter out hidden files
        if not l[0] == ".":
            # and files not ending with .json
            split = l.split(".")
            if split[len(split) - 1].lower() == 'epub':
                convert(l)

if __name__ == "__main__":
    run()