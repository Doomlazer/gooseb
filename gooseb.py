import os
import json
import random

def doPage(data,page):
    # banner text
    os.system('clear')
    print(str('\x1b[31m') + str(data["banner"]))
    print(str('\x1b[36m') + data["title"] + str('\x1b[35m') + " Page: " + str(page) + str('\x1b[0m') + str("\n"))
    print(data[str(page)])
    # add dice roll
    if (str(page) + "roll" in data):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        print('\x1b[37m' + f"Rolled {r1} & {r2}. Total: {(r1 + r2)}" + str('\x1b[0m\n'))
    # get input
    np = input(str('\x1b[36m') + "Enter page # or help: " + str('\x1b[0m'))
    try: 
        if (str(np) == "quit"):
            quit()
        elif (str(np) in data["namedPages"]):
            next = np
        elif (int(np) > 0 and int(np) <= data["length"]):
            next = np
        else:
            next = page
    except ValueError:
        next = page
    # show selected page
    doPage(data, next)


def run():
    books = os.listdir("./books")
    if len(books) < 1:
        print("No books found. Add .JSON files to 'books' folder and try again")
        quit()
    else:
        os.system('clear')
        print("Give Yourself GooseBumps Book Reader")
        print("By DoomLazer")
        print("Version 1.0 Nov. 2024")
        print("")
        i = 1
        for book in books:
            print(str(i) + ") " + book)
            i += 1
        print("")
        b = input(str('\x1b[36m') + "Select book to load: " + str('\x1b[0m'))
        if (int(b) < 1 or int(b) > len(books)):
            print("Invalid selection.")
            print("Goodbye...")
            quit()
        b = int(b) - 1
        with open('./books/' + str(books[b])) as f:
            data = json.load(f, strict=False)
        doPage(data, data["firstPage"])

if __name__ == "__main__":
	run()