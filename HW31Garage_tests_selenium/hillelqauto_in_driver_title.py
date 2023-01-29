import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


options = Options()
# options.add_argument("start-maximized"); # open Browser in maximized mode
# options.add_argument("disable-infobars"); # disabling infobars
# options.add_argument("--disable-extensions"); # disabling extensions
# options.add_argument("--disable-gpu"); # applicable to windows os only
# options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
# options.add_argument("--no-sandbox")
# options.add_argument("headless")

# START DRIVER
# driver = webdriver.Chrome('C:/Users/Owner/Downloads/chromedriver_win32/chromedriver.exe', options=options)
driver = webdriver.Chrome(service=Service('C:/Users/Owner/Downloads/chromedriver_win32/chromedriver.exe'), options=options)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://qauto2.forstudy.space/")

user = "guest"
password = "welcome2qauto"
driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")
# driver.get("https://qauto2.forstudy.space/")

# assert "Python1" in driver.title # Test fail
time.sleep(3) #sleep for 2 sec

assert "Hillel Qauto" in driver.title

# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class")
# find_element(By.CSS_SELECTOR, "css selector")
# elem = driver.find_element(By.CLASS, "header-link -guest")
# elem = driver.find_element(By.NAME, "q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# goButton = driver.find_element(By.ID, "submit")
# goButton.click()

# time.sleep(2) #sleep for 2 sec
# assert "No results found." not in driver.page_source
# driver.close()
