import os
import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.dashboard import Dashboard


class TestChangeLanguage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_changing_language_before_login_in(self):
        user_login = LoginPage(self.driver)
        # user_login.title_of_page()
        user_login.click_english_language_listbox()
        time.sleep(5)
        user_login.click_polski_language_option()
        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()