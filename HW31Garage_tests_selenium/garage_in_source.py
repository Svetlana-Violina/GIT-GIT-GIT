import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()

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

# assert "" in driver.current_url
# input =
# element = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout//div[2]/button[1]")
goButton = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout//div[2]/button[1]")
goButton.click()
time.sleep(2) #sleep for 2 sec
# email = "violina.svetlana@gmail.com"
# password = "rBMP18GMNkzNuR"
# driver.get("https://" + email + ":" + password + "@" + "qauto2.forstudy.space/")
# time.sleep(5) #sleep for 2 sec

assert "Garage" in driver.page_source

