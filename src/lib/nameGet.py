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
    randomNum = random.randint(1, 4944)
    return first_names[randomNum]

def getLast():
    with open(getPathLast()) as file:
        last_names = file.readlines()
        last_names = [name.strip() for name in last_names]
    randomNum = random.randint(1, 4944)
    return last_names[randomNum]

def randomName():
    name = getLast() + getFirst()
    return name