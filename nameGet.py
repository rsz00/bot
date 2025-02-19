import os
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


