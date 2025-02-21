import os
from lib import account

def write_credentials(username,password):
    with open(os.path.dirname(__file__)+"\cont\\credentials.txt","a") as file:
        file.write(username + "," + password + "\n")

def receive_credentials():
    with open(os.path.dirname(__file__)+"\cont\\credentials.txt","r") as file:
        lines = file.readlines()
        names = []
        passwords = []
        for line in lines:
            splitted_string = line.split(",")
            names.append(splitted_string[0].strip())
            passwords.append(splitted_string[1].strip())
    return account.generateAccountArray(names,passwords)
