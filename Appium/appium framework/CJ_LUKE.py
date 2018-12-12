import time
from subprocess import Popen

from appium import webdriver

import appium_helper as appHelp
from dyson_link_config import DysonLinkConfig
import log_test_message as log

log.logProgress(__file__, 'main', 'begin')
dysonLinkConfig = DysonLinkConfig()

desired_caps = {'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName': 'Samsung Galaxy S6',
                'app': 'path of the apps',
                'appPackage': 'package name',
                'appActivity': 'acticity name',
                # 'noReset': 'true',
                # 'cloudEnvironmentAndroid':'integration',
                'optionalIntentArguments': '--es Environment integration',
                # 'processArguments': '{"args":["-Environment mockShared, -TestSessionToken 2017-12-07_09-51-31-546870"]}',
                "autoGrantPermissions": 'true'
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

if (not appHelp.clickElementById(driver, 'getconnected_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after getconnected_button')
if (not appHelp.sendKeysToElementById(driver, 'textinput_left', 10, dysonLinkConfig.username)):
    exit()
log.logProgress(__file__, 'main', 'after username')
if (not appHelp.clickElementById(driver, 'next_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after next_button')
if (not appHelp.sendKeysToElementById(driver, 'textinput_left', 10, dysonLinkConfig.password)):
    exit()
log.logProgress(__file__, 'main', 'after password')
if (not appHelp.clickElementById(driver, 'proceed_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after proceed_button')
if (not appHelp.clickElementById(driver, 'navigation_menu_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after navigation_menu_button')
if (not appHelp.clickElementById(driver, 'add_machine_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after add_machine_button')
if (not appHelp.clickElementById(driver, 'next_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after next_button')
if (not appHelp.clickElementById(driver, 'next_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after next_button')
if (not appHelp.clickElementById(driver, 'next_button', 10)):
    exit()
log.logProgress(__file__, 'main', 'after next_button')

time.sleep(5)
#xpath = "//android.widget.TextView [@text ='" + dysonLinkConfig.machine_serial + "']" + "//following-sibling::TextView"
xpath = "//android.widget.TextView [@text ='" + dysonLinkConfig.machine_serial + "']"
print(xpath)
all_spans = driver.find_elements_by_xpath("//android.view.ViewGroup")
for span in all_spans:
    print (span.text)


