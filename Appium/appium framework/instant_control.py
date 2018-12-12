import os
import time
from subprocess import Popen

from appium import webdriver
from selenium.webdriver.common.by import By

import appium_helper as appHelp
import log_test_message as log
from dyson_link_config import DysonLinkButtonConfig
from dyson_link_config import DysonLinkConfig


def gotoLocationPage(driver, location, tries):
    try:
        for x in range(tries):
            print('try ' + str(x))
            if (not appHelp.waitForElementToContainSomeText(driver, By.ID, 'location_textview', 10)):
                return False

            element = appHelp.getElement(driver, By.ID, 'location_textview', 10)
            if (element.text == location):
                return True

            driver.swipe(900, 1500, 100, 1500)
            time.sleep(2)
        return False

    except Exception as ex:
        return False


log.logProgress(__file__, 'main', 'begin')

dysonLinkConfig = DysonLinkConfig()

desired_caps = {'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName': 'Samsung Galaxy S6',
                'appPackage': 'com.dyson.mobile.android.ble.weekly.debug',
                'appActivity': 'com.dyson.mobile.android.launch.LaunchActivity',
                'noReset': 'true',
                'fullReset': 'false'
                }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Remove original readings first
if os.path.exists('C:\\Temp\\reading.json'):
    os.remove('C:\\Temp\\reading.json')

if (not gotoLocationPage(driver, dysonLinkConfig.machine_location, 5)):
    exit()
log.logProgress(__file__, 'main', 'after goto machine location')
if (not appHelp.clickElement(driver, By.ID, 'oval_left_imageview', 10)):
    exit()
log.logProgress(__file__, 'main', 'after oval_left_imageview')
if (not appHelp.uncheckElement(driver, By.ID, 'power_toggle', 10)):
    exit()
log.logProgress(__file__, 'main', 'after switch off')

Popen("C:\\Users\\sli\\PycharmProjects\\appium framework\\Labview Scripts\\Readings\\TakeReadings.exe")
button_status = DysonLinkButtonConfig()
automode = DysonLinkButtonConfig.auto
try:
    if (automode == 'System OFF'):
        log.logProgress(__file__, 'main', 'Power button is off')
except Exception as ex:
    print(ex)
