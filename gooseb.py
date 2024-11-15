import os
import json
import random
# Text to Speech requires:
#   pip install py3-tts
import pyttsx3 

booksPath = os.path.dirname(os.path.realpath(__file__)) + '/books/'
speak = False
pageStack = []
data = []
tts = None
money = 0
monied = []

def doMoney():
    print()

def doPage(page):
    global money
    global monied
    global speak
    global data
    # banner text
    os.system('clear')
    print(str('\x1b[31m') + str(data["banner"]))
    print(str('\x1b[36m') + data["title"] + str('\x1b[35m') + " Page: " + str(page))
    # money
    if ("money" in data):
        if (str(page) + "money" in data):
            if not page in monied:
                money += data[str(page) + "money"]
                monied.append(page)
                print(monied)

        print(data["money"] + str(money) + str('\x1b[0m') + str("\n"))
    else:
        print(str('\x1b[0m') + str("\n"))

    print(data[str(page)])
    if speak:
        d = data[str(page)]
        if (str(page) + "speechtext" in data):
            d = data[str(page) + "speechtext"]
        tts.say(d)
        tts.runAndWait()
    # add dice roll
    if (str(page) + "roll" in data):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        print('\x1b[37m' + f"Rolled {r1} & {r2}. Total: {(r1 + r2)}" + str('\x1b[0m\n'))
        if speak:
            tts.say(f"Rolled {r1} & {r2}. Total: {(r1 + r2)}")
            tts.runAndWait()
    # get input
    np = input(str('\x1b[36m') + "Enter page # or help: " + str('\x1b[0m'))
    try: 
        if (str(np).lower() == "quit" or str(np).lower() == "q"):
            # exit
            quit()
        elif (str(np).lower() == "tts"):
            # text to speech toggle
            next = page
            speak = False if speak else True
        elif ((str(np).lower() == "prev" or str(np).lower() == "p") and len(pageStack) > 0):
            # step backward in page history
            next = pageStack.pop()
        elif (str(np).lower() in data["namedPages"]):
            # matched namedPages
            next = np
        elif (int(np) > 0 and int(np) <= data["length"]):
            # entry bounds
            next = np
        else:
            next = page
    except ValueError as e:
        print("Error:" + str(e))
        next = page
    if (not str(np).lower() == "prev") or (not str(np).lower() == "p"):
        pageStack.append(page)
    doPage(next)

def run():
    global data
    global tts
    tts = pyttsx3.init()
    #dirList = os.listdir("./books")
    dirList = os.listdir(booksPath)
    books = []
    for l in dirList:
        # filter out hidden files
        if not l[0] == ".":
            # and files not ending with .json
            split = l.split(".")
            if split[len(split) - 1].lower() == 'json':
                books.append(l)
    if len(books) < 1:
        print("No books found. Add .JSON files to 'books' folder and try again")
        quit()
    else:
        os.system('clear')
        print('\x1b[37m' + "Give Yourself GooseBumps Book Reader")
        print("By DoomLazer")
        print("Version A1.0 Nov. 2024")
        print(str('\x1b[0m'))
        i = 1
        for book in books:
            print(str(i) + ") " + book)
            i += 1
        print()
        b = input(str('\x1b[36m') + "Select book to load: " + str('\x1b[0m'))
        try:
            if (int(b) < 1 or int(b) > len(books)):
                print("Selected number not in range.")
                print("Goodbye...")
                quit()

            b = int(b) - 1
            with open(booksPath + str(books[b])) as f:
                data = json.load(f, strict=False)
            doPage(str(data["firstPage"]))
        except ValueError as e:
            print("Error: " + str(e))
            quit()

if __name__ == "__main__":
	run()