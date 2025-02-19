import random
def genUsername(first, last):
    randomNum = random.randint(1, 423)
    userName = first + "_" + last + randomNum
    return userName