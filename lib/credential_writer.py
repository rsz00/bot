import os


def write_credentials(username,password):
    with open(os.path.dirname(__file__)+"\cont\\credentials.txt","a") as file:
        file.write(username + "," + password + "\n")