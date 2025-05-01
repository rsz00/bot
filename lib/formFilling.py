from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import credential_writer
from selenium.common.exceptions import *
import time
import os
import random

def get_credentials_from_file(filepath):
    with open(filepath,"r") as file:
        return file.readline().strip()

def formFilling(driver):
    adress = "https://www.instagram.com/"
    driver.get(adress)
    driver.implicitly_wait(5)
    cookie_buttons = driver.find_elements(By.TAG_NAME,"button")
    for button in cookie_buttons:
        if button.text == "Optionale Cookies ablehnen":
            button.click()
    driver.implicitly_wait(7)

    #splitting string for data input
    credentials = get_credentials_from_file(os.path.dirname(__file__)+"\cont\\credentials.txt")
    userName, password = credentials.split(",",1)

    print(f"using credentials: {userName},{password}")

    #input username
    min_delay = 0.1
    max_delay = 0.3

    usernameField = driver.find_element(By.NAME, "username")
    for character in userName:
        usernameField.send_keys(character)
        time.sleep(random.uniform(min_delay, max_delay))
        
    #input password
    passwordField = driver.find_element(By.NAME, "password")
    for character in password:
        passwordField.send_keys(character)
        time.sleep(random.uniform(min_delay, max_delay))
    #login
    driver.implicitly_wait(5)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    time.sleep(1)
    for button in buttons:
        if button.text == "Anmelden":
            button.click()
    
formFilling(webdriver.Firefox())

