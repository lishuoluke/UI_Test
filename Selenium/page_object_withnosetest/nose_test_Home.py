import sys
from selenium import webdriver
import unittest
from time import sleep
import Config_Test as config
from Common_Function import click_to_login_page
from Common_Function import user_login
from Common_Function import press_home

class browser(unittest.TestCase):
    def setUp(self):

        self.config = config.TestAutomationConfig()

        self.browser = self.config.browser
        self.username = self.config.user
        self.pwd = self.config.pwd

        if (self.browser == '2'):
            driverLocation = './geckodriver'
            self.driver = webdriver.Firefox(executable_path=driverLocation)
        elif (self.browser == '1'):
            driverLocation = './chromedriver'
            self.driver=webdriver.Chrome(driverLocation)



    def test_scenario(self):

        click_to_login_page(self.driver)
        sleep(2)
        user_login(self.driver, self.username, self.pwd)
        sleep(3)
        press_home(self.driver)
        sleep(2)

    def doCleanups(self):
        self.driver.quit()
