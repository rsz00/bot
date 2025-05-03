from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib import emailGrabber
from lib import passGen
from lib import nameGet
from lib import credential_writer
from lib import randomMonth
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

    #weiter click
    driver.implicitly_wait(5)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    time.sleep(1)
    for button in buttons:
        if button.text == "Weiter":
            button.click()

    #enter Birthdate
    month = driver.find_element(By.CSS_SELECTOR, 'select._aau-._ap32[title="Monat:"]')
    month.click()
    randomMonthLogin = randomMonth.randomMonthGer()
    month.send_keys(randomMonthLogin)

    day = driver.find_element(By.CSS_SELECTOR, 'select._aau-._ap32[title="Tag:"]')
    day.click()
    day.send_keys(random.randint(1,28))

    year = driver.find_element(By.CSS_SELECTOR, 'select._aau-._ap32[title="Jahr:"]')
    year.click()
    year.send_keys(random.randint(1980,2004))

    #weiter click
    driver.implicitly_wait(5)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    time.sleep(1)
    for button in buttons:
        if button.text == "Weiter":
            button.click()
    time.sleep(2)
    
    #confirm email
    #click "Code erneute senden" to get the email
    buttons = driver.find_elements(By.TAG_NAME, "div")

    time.sleep(1)
    emailCode = None
    while emailCode == None:
        emailCode = emailGrabber.emailConfirm(browser)
        emailConfirm = driver.find_element(By.NAME, "email_confirmation_code")
        if emailCode == None:
            for button in buttons:
                    if button.text == "Code erneut senden.":
                        button.click()
            time.sleep(1)
            if emailCode != None:
                break
    emailConfirm.send_keys(emailCode)
    time.sleep(1)

    buttons = driver.find_elements(By.TAG_NAME, "div")
    for button in buttons:
        if button.text == "Weiter":
            try:
                button.click()
            except ElementClickInterceptedException:
                pass
    #saves bot login
    credential_writer.write_credentials(userName, password)
    
    time.sleep(1)
    browser.quit()
    driver.quit()


