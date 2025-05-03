from lib import formFilling
from lib import credentials_index
from selenium import webdriver
import os
import time

def login_with_next_account():
    # Define file paths
    credentials_file = os.path.join("d:\\Programme (x86)\\Projekte\\Bots\\bot\\lib\\cont", "credentials.txt")
    last_used_file = os.path.join("d:\\Programme (x86)\\Projekte\\Bots\\bot\\lib\\cont", "last_used.txt")

    # Get all credentials
    credentials = credentials_index.get_credentials(credentials_file)
    if not credentials:
        print("No credentials found!")
        return

    # Get the next account index
    next_index = credentials_index.get_next_account_index(last_used_file, len(credentials))

    # Get the username and password for the next account
    userName, password = credentials[next_index].split(",", 1)

    # Update the last used index
    credentials_index.update_last_used_index(last_used_file, next_index)

    # Initialize WebDriver and log in
    driver = webdriver.Firefox()
 
    formFilling.formFilling(driver, userName, password)

# Run the function
if __name__ == "__main__":
    login_with_next_account()