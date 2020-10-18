from selenium import (webdriver,
                      )
from selenium.webdriver.common.keys import Keys
import time


class InstaBot:

    def __init__(self, username, password, hashtag) -> None:
        """

        :param username: get a  user's username to login
        :param password: get a user's password to login

        """
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.hashtag = hashtag

    def close_browser(self) -> None:
        """ function to close browser"""
        self.driver.close()

    def login_into_instagram(self) -> None:
        """
        function to login into instagram

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

    def get_and_like_photo_by_tag(self):
        pass






