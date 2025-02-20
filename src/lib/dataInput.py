from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from emailGrabber import emailGrabber
from passGen import passGen
from nameGet import randomName 
from selenium.common.exceptions import *
import time

def dataInput(driver):
    adress = "https://www.instagram.com/accounts/emailsignup/"
    driver.get(adress)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]").click()
    driver.implicitly_wait(7)
    
    #input für email
    browser = webdriver.Firefox()
    email = emailGrabber(browser)
    driver.find_element(By.NAME, "emailOrPhone").send_keys(email)

    #input für password
    password = passGen()
    driver.find_element(By.NAME, "password").send_keys(password)

    #input für fullName
    fullName = randomName()
    driver.find_element(By.NAME, "fullName").send_keys(fullName)

    #input für username
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[7]/div/div/div/button/span").click()
    except NoSuchElementException:
        


    #weiter click
    driver.implicitly_wait(5)
    driver.find_elements(By.TAG_NAME, 'button')[3].click()




dataInput(webdriver.Firefox())

