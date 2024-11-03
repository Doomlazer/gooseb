import os
import json
import random
# Text to Speech requires:
#   pip install pyttsx4
# Also had to do:
#   pip install py3-tts
import pyttsx4

pageStack = []

def doPage(data,page,tts):
    # banner text
    os.system('clear')
    print(str('\x1b[31m') + str(data["banner"]))
    print(str('\x1b[36m') + data["title"] + str('\x1b[35m') + " Page: " + str(page) + str('\x1b[0m') + str("\n"))
    print(data[str(page)])
    tts.say(data[str(page)])
    tts.runAndWait()
    # add dice roll
    if (str(page) + "roll" in data):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        print('\x1b[37m' + f"Rolled {r1} & {r2}. Total: {(r1 + r2)}" + str('\x1b[0m\n'))
        tts.say(f"Rolled {r1} & {r2}. Total: {(r1 + r2)}")
        tts.runAndWait()
    # get input
    np = input(str('\x1b[36m') + "Enter page # or help: " + str('\x1b[0m'))
    try: 
        if (str(np).lower() == "quit" or str(np).lower() == "q"):
            quit()
        elif ((str(np).lower() == "prev" or str(np).lower() == "p") and len(pageStack) > 0):
            next = pageStack.pop()
        elif (str(np).lower() in data["namedPages"]):
            next = np
        elif (int(np) > 0 and int(np) <= data["length"]):
            next = np
        else:
            next = page
    except ValueError:
        next = page
    if (not str(np).lower() == "prev") or (not str(np).lower() == "p"):
        pageStack.append(page)
    doPage(data, next, tts)


def run():
    engine = pyttsx4.init()
    books = os.listdir("./books")
    if len(books) < 1:
        print("No books found. Add .JSON files to 'books' folder and try again")
        quit()
    else:
        os.system('clear')
        print('\x1b[37m' + "Give Yourself GooseBumps Book Reader Text to Speech")
        engine.say("Give Yourself GooseBumps Book Reader. Text to speech edition")
        engine.runAndWait()
        print("By DoomLazer")
        engine.say("By Doom Laser")
        engine.runAndWait()
        print("Version A1.0 Nov. 2024")
        print(str('\x1b[0m'))
        i = 1
        for book in books:
            print(str(i) + ") " + book)
            i += 1
        print("")
        b = input(str('\x1b[36m') + "Select book to load: " + str('\x1b[0m'))
        try:
            if (int(b) < 1 or int(b) > len(books)):
                print("Invalid selection.")
                print("Goodbye...")
                quit()
            b = int(b) - 1
            with open('./books/' + str(books[b])) as f:
                data = json.load(f, strict=False)
            doPage(data, data["firstPage"], engine)
        except ValueError:
            print("Selection too spooky; killing program...")
            quit()

if __name__ == "__main__":
	run()