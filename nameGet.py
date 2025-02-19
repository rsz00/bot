import os
import random
def getPathFirst():
    path = os.path.dirname(__file__)
    pathname = ("\cont\\first-names.txt")
    contdir = path + pathname
    return contdir

def getPathLast():
    path = os.path.dirname(__file__)
    pathname = ("\cont\\names.txt")
    contdir = path + pathname
    return contdir

def getFirst():
    with open(getPathFirst()) as file:
        first_names = file.readlines()
        first_names = [name.strip() for name in first_names]
    randFirst = random.randint(1, 4944)
    return first_names[randFirst]

print(getFirst())
    