from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "your@gmail.com"
TWITTER_PASSWORD = "your password"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_driver_path = r"C:\DEVELOPMENT\chromedriver_win32\chromedriver.exe"
        self.service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(By.XPATH,
                                      '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        time.sleep(60)
        downn = self.driver.find_element(By.XPATH,
                                         '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        upp = self.driver.find_element(By.XPATH,
                                       '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = downn.text
        self.up = upp.text

    def tweet_at_provider(self):
        text = f"Hey internet provider why is my internet speed down by {self.down} / {self.up} when i payed for {PROMISED_DOWN}/{PROMISED_UP}"
        self.driver.get("https://twitter.com/home?lang=en")
        time.sleep(3)
        login = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a/div')
        login.click()
        time.sleep(5)
        email_fill = self.driver.find_element(By.NAME, 'text')
        email_fill.send_keys(TWITTER_EMAIL)
        time.sleep(5)
        email_fill.send_keys(Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_element(By.NAME, "text")
        password.send_keys("zetooye")
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        password_m = self.driver.find_element(By.NAME, "password")
        password_m.send_keys(TWITTER_PASSWORD)
        password_m.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        tweet.send_keys(text)
        time.sleep(3)
        final = self.driver.find_element(By.XPATH, "//*[text()='Tweet']")
        final.click()
        time.sleep(1000)

speedtweet = InternetSpeedTwitterBot()

# speedtweet.get_internet_speed()
speedtweet.tweet_at_provider()
