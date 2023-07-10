from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from speed import InternetSpeedTwitterBot


speedtweet = InternetSpeedTwitterBot()

speedtweet.get_internet_speed()
speedtweet.tweet_at_provider()