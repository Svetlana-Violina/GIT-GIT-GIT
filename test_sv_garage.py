import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


def test_garage_in_source():
    options = Options()
    driver = webdriver.Chrome(service=Service('C:/Users/Owner/Downloads/chromedriver_win32/chromedriver.exe'), options=options)

    driver.get("https://qauto2.forstudy.space/")

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")
    time.sleep(3) #sleep for 2 sec

    goButton = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout//div[2]/button[1]")
    goButton.click()
    time.sleep(2) #sleep for 2 sec

    assert "Garage" in driver.page_source

def test_hillelqauto_in_driver_title():
    options = Options()
    driver = webdriver.Chrome(service=Service('C:/Users/Owner/Downloads/chromedriver_win32/chromedriver.exe'), options=options)

    driver.get("https://qauto2.forstudy.space/")

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")
    time.sleep(3)  # sleep for 2 sec

    assert "Hillel Qauto" in driver.title

def test_instructions_in_source():
    options = Options()
    driver = webdriver.Chrome(service=Service('C:/Users/Owner/Downloads/chromedriver_win32/chromedriver.exe'),
                              options=options)

    driver.get("https://qauto2.forstudy.space/")

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")
    time.sleep(3)  # sleep for 2 sec

    goButton = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout//div[2]/button[1]")
    goButton.click()
    time.sleep(2)  # sleep for 2 sec

    assert "Instructions" in driver.page_source

def test_qauto_in_url():
    options = Options()
    driver = webdriver.Chrome(service=Service('C:/Users/Owner/Downloads/chromedriver_win32/chromedriver.exe'),
                              options=options)

    driver.get("https://qauto2.forstudy.space/")

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")
    time.sleep(3)  # sleep for 2 sec

    assert "qauto2.forstudy" in driver.current_url

def test_school_in_source():
    options = Options()
    driver = webdriver.Chrome(service=Service('C:/Users/Owner/Downloads/chromedriver_win32/chromedriver.exe'), options=options)

    driver.get("https://qauto2.forstudy.space/")

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")
    time.sleep(2)  # sleep for 2 sec

    goButton = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout//div[2]/button[1]")
    goButton.click()
    time.sleep(2)

    assert "Hillel IT school" in driver.page_source
