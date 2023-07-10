from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "your@gmail.com"
TWITTER_PASSWORD = "yourpassword"
CHROME_WEBDRIVER_PATH = r"C:\DEVELOPMENT\chromedriver_win32\chromedriver.exe"
SPEED_TEST_URL = "https://www.speedtest.net/"
login = "https://twitter.com/i/flow/login"
TWITTER_URL = login


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.service = Service(CHROME_WEBDRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(60)
        go_button = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(3)
        account = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        account.send_keys(TWITTER_EMAIL)
        time.sleep(5)
        account.send_keys(Keys.ENTER)
        time.sleep(3)
        password = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(5)
        password.send_keys(Keys.ENTER)
        time.sleep(20)

        compose_tweet = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        compose_tweet.click()
        time.sleep(30)

        tweet = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(5)

        tweet_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_button.click()

        time.sleep(10)
        self.driver.quit()


auto_complaining_boot = InternetSpeedTwitterBot()
auto_complaining_boot.get_internet_speed()
auto_complaining_boot.tweet_at_provider()
