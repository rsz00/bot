from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re

#grabs email
def emailGrabber(driver):
    urlEmail = "https://anonymmail.net/"
    driver.get(urlEmail)
    driver.implicitly_wait(7)
    email = driver.find_element(By.CLASS_NAME, "email")
    return email.text

#gets confirmation code from email
def emailConfirm(driver):
    driver.implicitly_wait(120)
    emailText = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/a[2]/div/div[4]/b").text
    emailCode = re.findall(r"\d+", emailText)
    return emailCode   