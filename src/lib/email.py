from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def emailName():
    service = service()
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/")

emailName()
    
