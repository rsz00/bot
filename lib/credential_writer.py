import os
from lib import account

def write_credentials(username,password):
    with open(os.path.dirname(__file__)+"\cont\\credentials.txt","a") as file:
        file.write(f"{username},{password}\n")

def receive_credentials():
    with open(os.path.dirname(__file__)+"\cont\\credentials.txt","r") as file:
        lines = file.readlines()
        splitted_string = lines.split(",")
        names = (splitted_string[0].strip())
        passwords =(splitted_string[1].strip())
    return account.generateAccountArray(names,passwords)