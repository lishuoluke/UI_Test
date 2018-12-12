# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import Config_Test as config


class Page(object):
    """基础类，用于所以页面对象类继承"""
    login_url = 'http://39.107.28.67:8080'

    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        #return self.driver.current_url == (self.base_url + self.url)
        return self.driver.current_url == self.url

    def _open(self, url):
        #url = self.base_url + url # Changed this as the login page has total different address as click login
        self.driver.get(url)
        #assert self.on_page(), 'did not land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)




class Mainpage(Page):
    "First Page after browse"
    config = config.TestAutomationConfig() # read content from config file

    mainpage =  config.mainpage # get the mainpage url

    url = mainpage
    #url = 'http://39.107.28.67:8080'

    languageselector_loc = (By.CSS_SELECTOR,config.languageselector)
    loginbutton_loc = (By.CSS_SELECTOR, config.loginarrow)
    logintag_loc = (By.CSS_SELECTOR, config.loginbutton)

    language = config.language
    if language =='1':
        language_loc = (By.CSS_SELECTOR, config.chilan)
    if language =='2':
        language_loc = (By.CSS_SELECTOR, config.englan)
    if language =='3':
        language_loc = (By.CSS_SELECTOR, config.ruslan)

    def type_clicklanguage(self):
        self.find_element(*self.languageselector_loc).click()

    def type_chooselanguage(self):
        self.find_element(*self.language_loc).click()

    def type_clicbutton(self):
        self.find_element(*self.loginbutton_loc).click()

    def type_clicktag(self):
        self.find_element(*self.logintag_loc).click()

class LoginPage(Page):
    """登录页面模型"""

    config = config.TestAutomationConfig() # read content from config file

    loginpage =  config.login # get the mainpage url

    url = loginpage
    #url = 'http://47.106.151.197:9999/login?service=http%3A%2F%2F39.107.28.67%3A8080%2Fuser%2Fdashboard.htm'
    # 定位器
    username_loc = (By.ID, config.username)
    password_loc = (By.ID, config.password)
    submit_loc = (By.ID, config.submit)

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)
        #print ('username typed')
    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)
        #print ('password typed')

    def type_submit(self):
        self.find_element(*self.submit_loc).click()
        #print('submit pressed')

class MainDashboard(Page):

    config = config.TestAutomationConfig() # read content from config file

    maindashboard = config.maindashboard
    language = config.language
    # get the mainpage url

    url = maindashboard
    #url = 'http://39.107.28.67:8080/user/dashboard.htm'
    # 定位器
    home_loc = (By.CSS_SELECTOR,config.home)
    dashboard_loc = (By.CSS_SELECTOR, config.dashboard)
    settings_loc = (By.CSS_SELECTOR, config.settings)
    statistics_loc = (By.CSS_SELECTOR, config.statistics)
    announcement_loc = (By.CSS_SELECTOR, config.announcement)
    if language =='1':
        Home = config.Chinese_Home
        Dashboard = config.Chinese_Dashboard
        Settings =  config.Chinese_Settings
        Satistics = config.Chinese_Statistics
        Annoucement = config.Chinese_Announcement

    if language =='2':
        Home = config.English_Home
        Dashboard = config.English_Dashboard
        Settings =  config.English_Settings
        Satistics = config.English_Statistics
        Annoucement = config.English_Announcement

    if language =='3':
        Home = config.Russian_Home
        Dashboard = config.Russian_Dashboard
        Settings =  config.Russian_Settings
        Satistics = config.Russian_Statistics
        Annoucement = config.Russian_Announcement

    def type_clicksetting(self):
        self.find_element(*self.settings_loc).click()
        #print('settings clicked')

    def type_clickhome(self):
        self.find_element(*self.home_loc).click()
        #print('home clicked')

    def type_clickdashboard(self):
        self.find_element(*self.dashboard_loc).click()
        #print('dashboard clicked')

    def type_clickstatistics(self):
        self.find_element(*self.statistics_loc).click()
        #print('statistics clicked')

    def type_clickannouncement(self):
        self.find_element(*self.announcement_loc).click()
        #print('announcement clicked')
    def type_gethometext(self):
        a =self.find_element(*self.home_loc).text
        return a
        #print('home clicked')