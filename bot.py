from selenium import (webdriver,
                     )
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time
import random
from data import hashtags


class InstaBot:

    def __init__(self, username, password) -> None:
        """

        :param username: get a  user's username to login
        :param password: get a user's password to login

        """
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.hashtag = random.choice(hashtags)

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

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                         '//*[@class="cmbtv"]'))).click()

    def get_and_like_photo_by_tag(self) -> None:
        """
        function to get  results for random  tag and like it.
        :return None

        """
        picture_valid_hrefs = []
        self.driver.get('https://www.instagram.com/explore/tags/'+self.hashtag+'/')

        for _ in range(7):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                WebDriverWait(self.driver, 5).until(EC.element_located_to_be_selected((By.TAG_NAME,'a')))
                elements_available_in_view = self.driver.find_elements_by_tag_name('a')
                pic_references_available_in_view = [element.get_attribute('href')
                                                    for element in elements_available_in_view
                                                    if '/p/' in element.get_attribute('href')]
                [picture_valid_hrefs.append(element) for element in pic_references_available_in_view
                 if element not in picture_valid_hrefs]

            except Exception:
                continue

            for picture_reference in pic_references_available_in_view:
                self.driver.get('https://www.instagram.com/' + picture_reference)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    time.sleep(random.randint(2, 4))
                    like_button = self.driver.find_element_by_xpath('//span[@aria-label="Like"]')
                    like_button().click()
                except Exception:
                        continue


    def follow_users(self):
        pass









