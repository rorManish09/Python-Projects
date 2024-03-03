# This program works only for Version Released on Feb 2024

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
ANY_ACCOUNT = "rashmika_mandanna" #Change according to you 
USERNAME = "Your User Name"
PASSWORD = "Your Password"

class InstaFollowwer:

    def __init__(self):

        self.driver =webdriver.Chrome(options)

    def login(self):

        self.driver.get("https://instagram.com")
        time.sleep(5)
        try:
            username_fld = self.driver.find_element(By.NAME,"username")
            username_fld.send_keys(USERNAME)

            time.sleep(1)

            password_fld = self.driver.find_element(By.NAME,"password")
            password_fld.send_keys(PASSWORD)

            time.sleep(1)

            login_btn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
            login_btn.click()
        except NoSuchElementException:
            print("This program works only for version 2024 feb of Insta web: Mail me to update code
            ")

        #Not now
        time.sleep(10)

        save_info_dialog = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        if save_info_dialog:
            save_info_dialog.click()

        time.sleep(10)
        #Not now
        turn_noti = self.driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]")

        turn_noti.send_keys(Keys.TAB)
        time.sleep(1)
        not_now = self.driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        not_now.send_keys(Keys.ENTER)

        time.sleep(10)
    def find_followers(self):

        #Search Btn
        search_btn = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div")
        search_btn.click()
        time.sleep(3)

        #Search field

        search_field = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
        search_field.send_keys(ANY_ACCOUNT)
        time.sleep(5)
        #choose Account

        account = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]")
        account.click()
        time.sleep(5)
        #Followers

        followers = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(10)
        #follow




    def follow(self):

        div = self.driver.find_element(By.XPATH,value="/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]")
        button = div.find_element(By.TAG_NAME,"button")
        time.sleep(10)
        for element in button:

            try:
                element.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element(By.XPATH,"//contains[text(),'Cancel')]")
                cancel_btn.click()
bot = InstaFollowwer()

bot.login()
bot.find_followers()
bot.follow()
