
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

booksPath = os.path.dirname(os.path.realpath(__file__)) + '/books/'

def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    # remove leading " "
    text.pop(0)
    return '\n\n'.join(text) + '\n'

def SEchapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return ' '.join(text)[2:] + '\n'

def convert(f):
    print("converting: " + f)
    book = epub.read_epub(booksPath + f)
    #creator = book.get_metadata('DC', 'creator')[0]
    title = book.get_metadata('DC', 'title')
    namedPages = ["help","description"]
    se = False
    if len(title) < 1:
        se = True
        title = f
        description = "To Do: fix description for Trapped in the Circus"
        items = list(book.get_items_of_type(ebooklib.ITEM_UNKNOWN))
    else:
        title = title[0][0]
        description = book.get_metadata('DC', 'description')[0][0]
        items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

    # get chapters from ePub
    chapters = []
    for i in items:
        #print(i.get_name())
        if '_ch' in i.get_name():
            chapters.append(i)
        # for Special Edition check for page_[num].html, not every page has html
        if 'page_' in i.get_name():
            if '.html' in i.get_name():
                if 'page_2.' in i.get_name():
                    # probably wrong
                    description = str(i .get_content())
                chapters.append(i)

    # use module to parse html
    entries = []
    for c in chapters:
        if se:
            entries.append(SEchapter_to_str(c))
        else:
            entries.append(chapter_to_str(c))

    # pack required keys and text
    fileData = {}
    fileData['banner'] = "R.L. Stine's Give Yourself Goosebumps"
    fileData['title'] = str(title)
    fileData['length'] = len(chapters)
    fileData['namedPages'] = namedPages
    fileData['help'] = "Commands: description, prev, quit"
    fileData['firstPage'] = 'description'
    
    for x in range(len(entries)):
        fileData[x-7 if se else x] = str(entries[x])
        # text spans two pages
        if x-7 == 3 and se:
            fileData[x-8] = str(fileData[x-8]) + str(entries[x])
        if x-7 == -6 and se:
            description = str(entries[x])
    fileData['description'] = description

    #print(fileData)
    json_object = json.dumps(fileData, indent=4)

    # Write json file
    with open(booksPath + f[:-5] + ".json", "w") as outfile:
        outfile.write(json_object)


def run():
    dirList = os.listdir(booksPath)
    for l in dirList:
        # filter out hidden files
        if not l[0] == ".":
            # and files not ending with .json
            split = l.split(".")
            if split[len(split) - 1].lower() == 'epub':
                convert(l)

if __name__ == "__main__":
    run()