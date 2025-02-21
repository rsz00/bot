from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib import emailGrabber
from lib import passGen
from lib import nameGet
from lib import credential_writer
from selenium.common.exceptions import *
import time
import random


def dataInput(driver):
    adress = "https://www.instagram.com/accounts/emailsignup/"
    driver.get(adress)
    driver.implicitly_wait(5)
    cookie_buttons = driver.find_elements(By.TAG_NAME,"button")
    for button in cookie_buttons:
        if button.text == "Optionale Cookies ablehnen":
            button.click()
    driver.implicitly_wait(7)
    
    #input für email
    browser = webdriver.Firefox()
    email = emailGrabber.emailGrabber(browser)
    driver.find_element(By.NAME, "emailOrPhone").send_keys(email)

    #input für password
    password = passGen.passGen()
    driver.find_element(By.NAME, "password").send_keys(password)

    #input für fullName
    name = nameGet.randomName()
    driver.find_element(By.NAME, "fullName").send_keys(name[0] + " " + name[1])

    #input für username
    userName = nameGet.genUsername(name[0], name[1])
    driver.find_element(By.NAME, "username").send_keys(userName)
    
    #saves bot login
    credential_writer.write_credentials(userName, password)

    #weiter click
    driver.implicitly_wait(5)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    time.sleep(1)
    for button in buttons:
        if button.text == "Weiter":
            button.click()

    #enter Birthdate
    month = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[1]/div/div[4]/div/div/span/span[1]/select")
    month.click()
    month.send_keys(randomMonth[random.randint(1,12)])


