import time
from subprocess import Popen

from appium import webdriver
from selenium.webdriver.common.by import By

import appium_helper as appHelp
import log_test_message as log
from dyson_link_config import DysonLinkConfig


def clickMachineElement(driver, prefix, machineSerial, tries):
    try:
        for x in range(tries):
            print('try ' + str(x))
            elements = driver.find_elements_by_class_name('android.widget.TextView')
            for index in range(len(elements) - 1):
                if (elements[index].text.startswith(prefix) and elements[index + 1].text == machineSerial):
                    appHelp.click(elements[index + 1])
                    return True

            #driver.swipe(500, 1500, 500, 1000)
            appHelp.swipeUp(driver, By.ID,'machine_list',10)
            time.sleep(2)
        return False

    except Exception as ex:
        return False


log.logProgress(__file__, 'main', 'begin')

dysonLinkConfig = DysonLinkConfig()

desired_caps = {'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName': 'Samsung Galaxy S6',
                #'app': 'C:\\Users\\sli\\pycharmprojects\\appium framework\\DysonLink-ble-debug.apk',
                'appPackage': 'com.dyson.mobile.android.ble.weekly.debug',
                'appActivity': 'com.dyson.mobile.android.launch.LaunchActivity',
                # 'noReset': 'true',
                # 'cloudEnvironmentAndroid':'integration',
                'optionalIntentArguments': '--es Environment integration',
                # 'processArguments': '{"args":["-Environment mockShared, -TestSessionToken 2017-12-07_09-51-31-546870"]}',
                "autoGrantPermissions": 'true'
                }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

if (not appHelp.clickElement(driver, By.ID, 'getconnected_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after getconnected_button')
if (not appHelp.setTextForElement(driver, By.ID, 'textinput_left', 10, dysonLinkConfig.username)):
    exit()
log.logProgress(__file__, 'main', 'after username')
if (not appHelp.clickElement(driver, By.ID, 'next_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after next_button')
if (not appHelp.setPasswordForElement(driver, By.ID, 'textinput_left', 10, dysonLinkConfig.password)):
    exit()
log.logProgress(__file__, 'main', 'after password')
if (not appHelp.clickElement(driver, By.ID, 'proceed_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after proceed_button')
if (not appHelp.clickElement(driver, By.ID, 'navigation_menu_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after navigation_menu_button')
if (not appHelp.clickElement(driver, By.ID, 'add_machine_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after add_machine_button')
if (not appHelp.clickElementAndWaitContentChanged(driver, By.ID, 'next_button', 'title_label', 10)):
    exit()
log.logProgress(__file__, 'main', 'after next_button')
if (not appHelp.clickElementAndWaitContentChanged(driver, By.ID, 'next_button', 'title_label', 10)):
    exit()
log.logProgress(__file__, 'main', 'after next_button')
if (not appHelp.clickElement(driver, By.ID, 'next_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after next_button')
appHelp.waitForElementToDisappear(driver, By.ID, 'spinner', 10)
log.logProgress(__file__, 'main', 'after spinner disappear')
if (not clickMachineElement(driver, dysonLinkConfig.prefix, dysonLinkConfig.machine_serial, 5)):
    exit()
log.logProgress(__file__, 'main', 'after machine selected')

time.sleep(20)
#Popen("C:\\Users\\sli\\PycharmProjects\\appium framework\\Labview Scripts\\Pressbutton\\PressButton.exe")
log.logProgress(__file__, 'main', 'after launching PCbutton.exe')

if (not appHelp.clickElement(driver, By.ID, 'next_button', 180)):
    exit()
log.logProgress(__file__, 'main', 'after next_button')
if (not appHelp.setPasswordForElement(driver, By.ID, 'textinput_left', 10, dysonLinkConfig.WIFI_password)):
    exit()
log.logProgress(__file__, 'main', 'after WIFI_password')
if (not appHelp.clickElement(driver, By.ID, 'next_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after next_button')
time.sleep(20)
