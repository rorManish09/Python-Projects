# This code works only for version working in Feb 2024
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

USER_ID = "YOUR USER ID / EMAIL OR PHONE"
PassWord = "YOUR PASSWORD"
URL = "https://www.linkedin.com/login"
driver.get(url=URL)
time.sleep(10)
userId_field = driver.find_element(By.ID,value="username")

userId_field.send_keys(USER_ID)

passwordField = driver.find_element(By.ID,value="password")

passwordField.send_keys(PassWord)

signIn_btn = driver.find_element(By.CSS_SELECTOR,value=".login__form_action_container button")
signIn_btn.click()
#
#IF CAPTCHA APPEARED YOU HAVE 60 SEC TO FILL IT

time.sleep(60)

jobSearch_label = driver.find_element(By.XPATH,value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')

jobSearch_label.click()
time.sleep(5)
jobSearch_field = driver.find_element(By.XPATH,value="/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]")
jobSearch_field.click()

# TYPE OF JOB
jobSearch_field.send_keys("Python Developer")
time.sleep(1)
jobSearch_field.send_keys(Keys.ARROW_DOWN)
jobSearch_field.send_keys(Keys.ESCAPE)
attribute = jobSearch_field.get_attribute("id").split("-")

time.sleep(2)
job_location_searchBar = driver.find_element(By.ID,value=f"jobs-search-box-location-id-{attribute[5]}")
job_location_searchBar.click()

# LOCATION OF JOB-------------------
job_location_searchBar.send_keys("London, England, United Kingdom") #<---- CHANGE YOUR LOCATION HERE
job_location_searchBar.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
job_location_searchBar.send_keys(Keys.ENTER)
time.sleep(10)
