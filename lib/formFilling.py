from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import credential_writer
from selenium.common.exceptions import *
import time
import os
import random
import credentials_index

def formFilling(driver, userName, password):
    adress = "https://www.instagram.com/"
    driver.get(adress)
    driver.implicitly_wait(5)

    # handle cookies
    cookie_buttons = driver.find_elements(By.TAG_NAME,"button")
    for button in cookie_buttons:
        if button.text == "Optionale Cookies ablehnen":
            button.click()
    driver.implicitly_wait(7)

    print(f"using credentials: {userName},{password}")

    # input username
    min_delay = 0.1
    max_delay = 0.3

    usernameField = driver.find_element(By.NAME, "username")
    for character in userName:
        usernameField.send_keys(character)
        time.sleep(random.uniform(min_delay, max_delay))
        
    # input password
    passwordField = driver.find_element(By.NAME, "password")
    for character in password:
        passwordField.send_keys(character)
        time.sleep(random.uniform(min_delay, max_delay))
    # login
    driver.implicitly_wait(5)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    time.sleep(1)
    for button in buttons:
        if button.text == "Anmelden":
            button.click()
    
if __name__ == "__main__":
    credentials_file = os.path.join(os.path.dirname(__file__), "cont", "credentials.txt")
    last_used_file = os.path.join(os.path.dirname(__file__), "cont", "last_used.txt")

    # get all credentials
    credentials = credentials_index.get_credentials(credentials_file)
    if not credentials:
        print("No credentials found!")
        exit()
    # get the next account index
    next_index = credentials_index.get_next_account_index(last_used_file, len(credentials))

    # split credentials into username and password
    userName, password = credentials[next_index].split(",", 1)

    # update the last used index
    credentials_index.update_last_used_index(last_used_file, next_index)

    driver = webdriver.Firefox()

    formFilling(driver, userName, password)



