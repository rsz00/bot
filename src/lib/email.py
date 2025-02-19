from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import os

def emailName():
    # Absoluten Pfad zum aktuellen Verzeichnis ermitteln
    geckopath = os.path.abspath(os.path.dirname(__file__))
    # Pfad zum Geckodriver angeben
    service = Service(f"{geckopath}\\geckodriver.exe")
    # Firefox-Webdriver mit dem angegebenen Service starten
    driver = webdriver.Firefox(service=service)
    # Webseite öffnen
    driver.get("https://www.google.com/")
    # Browser schließen
    driver.quit()

emailName()