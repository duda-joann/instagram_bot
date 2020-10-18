from selenium import (webdriver,
                      )
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def close_browser(self) -> None:
        self.driver.close()

    def login_into_instagram(self) -> None:
        """
        login xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        password xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'

        """
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        username_field = self.driver.find_element_by_xpath('//input[@name="username"]')
        password_field = self.driver.find_element_by_xpath('//input[@name="password"]')
        username_field.clear()
        username_field.send_keys(self.username)
        password_field.clear()
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)