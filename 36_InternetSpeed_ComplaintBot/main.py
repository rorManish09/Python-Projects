#This code works for twitter verison 2024 feb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
DOWN_SPEED_UPTO = 100
UP_SPEED_UPTO = 20
TWITTER_EMAIL = "Your user id either email or number"
TWITTER_PASSWORD = "Your Password"
TWITTER_USERNAME = 'Your Username'

class InternetSpeedTwitterBot:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options)
        self.up=0
        self.down=0
    def get_internet_speed(self):
        pass
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        continue_btn = self.driver.find_element(By.ID,"onetrust-accept-btn-handler")
        continue_btn.click()
        time.sleep(5)
        go_btn = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_btn.click()
        time.sleep(60)

        try:

            close_btn = self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
            close_btn.click()
            time.sleep(5)
            down_speed = self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
            up_speed = self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            print("Down speed:"+down_speed)
            print("Up Speed:"+up_speed)
        except NoSuchElementException :
            down_speed = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
            up_speed = self.driver.find_element(By.XPATH,
                                                '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            print("Down speed:" + down_speed)
            print("Up Speed:" + up_speed)


    def tweet_at_provider(self):


        self.driver.get("https://www.twitter.com/i/flow/login")
        time.sleep(10)
        user_id = self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user_id.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        next_btn = self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_btn.click()
        time.sleep(5)
        try:
            security_checkup = self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            security_checkup.send_keys(TWITTER_USERNAME)
            time.sleep(2)
            security_next_btn = self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
            security_next_btn.click()

            time.sleep(5)
            password_fld1 = self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_fld1.send_keys(TWITTER_PASSWORD)
            time.sleep(1)
            password_fld1.send_keys(Keys.ENTER)
            time.sleep(10)

            try:
                time.sleep(5)
                password_fld1 = self.driver.find_element(By.XPATH,
                                                         '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
                password_fld1.send_keys(TWITTER_PASSWORD)
                time.sleep(1)
                password_fld1.send_keys(Keys.ENTER)
                time.sleep(10)
            except:
                pass

        except NoSuchElementException:
            time.sleep(5)
            password_fld = self.driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_fld.send_keys(TWITTER_PASSWORD)
            time.sleep(1)
            password_fld.send_keys(Keys.ENTER)
            time.sleep(10)

        post_field = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div')
        time.sleep(1)
        post_field.click()
        post_field.send_keys(f"Hey internet provider why my internet speed is {self.down} Down/{self.up} UP, when I pay for {DOWN_SPEED_UPTO} Down/ {UP_SPEED_UPTO} UP")
        time.sleep(1)

        post_btn = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        time.sleep(1)
        post_btn.click()
bot = InternetSpeedTwitterBot()



bot.get_internet_speed()
bot.tweet_at_provider()
