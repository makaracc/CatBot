import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Here is where you can change your login and targetUser
# TODO: Edit the login and targetUser.
yourUsername = ""
yourPassword = ""
targetUsername = ""

# Get a Cat img from api.thecatapi.com
request = requests.get("https://api.thecatapi.com/v1/images/search")
data = request.json()
imgUrl = request.json()[0]['url']

# Message to send
message = "Here is a random cat pic: " + imgUrl

# Bot Class
class InstaCatBot:
  def __init__(self, username, password, targetUser, message):
    self.username = username
    self.password = password
    self.targetUser = targetUser
    self.message = message
    # Chrome Driver
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.base_url = "https://www.instagram.com/"
    
  def start(self):
    self.driver.get(self.base_url)
    # Username
    enter_username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    enter_username.send_keys(self.username)
    # Password
    enter_password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    enter_password.send_keys(self.password)
    time.sleep(5)
    # Login
    self.driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(3)
    # Save info?
    self.driver.find_element_by_class_name('y3zKF').click()
    time.sleep(4)
    # Turn on notifications? Not now
    self.driver.find_element_by_class_name('HoLwm').click()
    time.sleep(4)
    # Go to profile
    self.driver.get(self.base_url + self.targetUser)
    time.sleep(3)
    # Chick on message
    self.driver.find_element_by_class_name('_8A5w5').click()
    time.sleep(4)
    # Find Message box and send message
    self.driver.find_element_by_css_selector('textarea[placeholder="Message..."]').send_keys(self.message)
    self.driver.find_element_by_css_selector('textarea[placeholder="Message..."]').send_keys(Keys.ENTER)
    time.sleep(2)
    
instaBot = InstaCatBot(yourUsername, yourPassword, targetUsername, message)
instaBot.start()