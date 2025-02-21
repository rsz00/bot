from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib import emailGrabber
from lib import passGen
from lib import nameGet
from selenium.common.exceptions import *
import time


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
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[7]/div/div/div/button/span").click()
    except NoSuchElementException:
        driver.find_element(By.NAME, "username").send_keys(nameGet.genUsername(name[0], name[1]))
    
    #weiter click
    driver.implicitly_wait(5)
    #for _ in range(3):
    buttons = driver.find_elements(By.TAG_NAME, "button")
    time.sleep(1)
    for button in buttons:
        print(button.text)
        if button.text == "Weiter":
            button.click()
            

