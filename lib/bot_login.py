from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(driver,usrname,psswd):
    driver.get("https://www.instagram.com/")
    driver.implicitly_wait(10)
    #click cookies
    buttons = driver.find_elements(By.TAG_NAME,"button")
    for button in buttons:
        if button.text == "Optionale Cookies ablehnen":
            button.click()
    inputs = driver.find_elements(By.TAG_NAME,"input")
    for field in inputs:
        if field.get_attribute("name") == "username":
            field.send_keys(usrname)
        if field.get_attribute("name") == "password":
            field.send_keys(psswd)
    div_elems = driver.find_elements(By.TAG_NAME,"div")
    for div in div_elems:
        if div.text == "Anmelden":
            div.click()
            break
