import ctypes  # An included library with Python install.
import json
import time
import datetime
import os

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from subprocess import Popen

# Returns abs path relative to this file and not cwd


desired_caps = {'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName':'Samsung Galaxy S6',
                'app':'C:\\Users\\sli\\pycharmprojects\\appium framework\\DysonLink-ble-debug.apk',
                'appPackage': 'com.dyson.mobile.android.ble.weekly.debug',
                'appActivity': 'com.dyson.mobile.android.launch.LaunchActivity',
                'noReset': 'true',
                #'cloudEnvironmentAndroid':'integration',
                #'optionalIntentArguments': '--es Environment integration',
                #'processArguments': '{"args":["-Environment mockShared, -TestSessionToken 2017-12-07_09-51-31-546870"]}',
                "autoGrantPermissions" : 'true'

}
#Define pop up window
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

#Define driver
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)



#Assign machine name and serioal numbers
with open('C:\\Users\\sli\\PycharmProjects\\appium framework\\config.json', 'r+') as configFile:
    config = json.load(configFile)
    machine_serial= config['Machine Serial']
    testResultFolder = config['testResultFolder']
    username = config['User Name']
    password = config['Password']
    WIFI_password = config['WIFI password']
    prefix =config['Machine Prefix']



#print(machine_serial)

## This is used to shake the devide for the SI server to set Region

#Mbox('Reminder', 'Set location and Environments, you have 10 seconds', 1)
time.sleep(1)

#Prepare Log file
startTime = datetime.datetime.now().strftime("%I_%M_%S_%p_%B_%d_%Y")
reportPath = testResultFolder + '\\' + 'Reports'
if not os.path.exists(reportPath):
    os.makedirs(reportPath)
filename = 'Log ' + startTime + '.txt'
reportFile = open(reportPath + '\\' + filename, 'w')
reportFile.write('This log is for machine with serial number ' + machine_serial + '\n')
reportFile.write('Log starts at ' + startTime + '\n')


#Log in
try:
    el0 = driver.find_element_by_id('getconnected_button')
    el0.click()
    time.sleep(2)
    el1 = driver.find_element_by_id('textinput_left')
    el1.send_keys(username)
    time.sleep(3)
    el2 = driver.find_element_by_id('next_button')
    el2.click()
    time.sleep(3)
    el3 = driver.find_element_by_id('textinput_left')
    el3.send_keys(password)
    time.sleep(1)
    el4 = driver.find_element_by_id('proceed_button')
    el4.click()
except:
    reportFile.write('Log in -- fail\n')

#Log in completed

#Mbox('Reminder', 'Connection Journey will start shortly', 1)

#Define a function for button pressing, if can find the button, then press it; it not then quit
def clickButton(reportFile, buttonId):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, buttonId)))
        element=driver.find_element_by_id(buttonId)
        element.click()
        reportFile.write(buttonId + ' -- success\n')
        return True
    except:
        reportFile.write(buttonId + ' -- fail\n')
        return False


#Go to Menu and Press the button to add machine


if (clickButton(reportFile,"navigation_menu_button") == False):
    exit()
if (clickButton(reportFile, "add_machine_button") == False):
    exit()

#if (clickButton(reportFile,"enable_location_button") == False):
#exit()
'''
time.sleep(3)
location = driver.find_element_by_id("enable_location_button")
location.click()
'''
#Popen("C:\\Users\\sli\\Desktop\\520 scripts\\TAB1.bat")

if (clickButton(reportFile,"next_button")== False):
    exit()
if (clickButton(reportFile, "next_button") == False):
    exit()
if (clickButton(reportFile, "next_button") == False):
    exit()

#xpath="//android.widget.TextView [@text ='"+ machine_serial + "']"
#print(xpath)
time.sleep(10)
all_spans = driver.find_elements_by_class_name('android.widget.TextView')

for x in range(len(all_spans)-1):
    if all_spans[x].text.startswith(prefix) and all_spans[x+1].text == machine_serial:
        all_spans[x].click()


'''
print('Wait for the press power icon')
time.sleep(30)
print('Before PCbutton')
Popen("C:\\Users\\sli\\PycharmProjects\\appium framework\\Labview Scripts\\Pressbutton\\PCbutton.exe")
print('After PCbutton')
#time.sleep(10)
#Mbox('Reminder', 'Completed!!!!', 1)



time.sleep(15)
print('Before click next_button')
if (clickButton(reportFile, "next_button") == False):
    exit()
print('After click next_button')

time.sleep(5)
el5 = driver.find_element_by_id('textinput_left')
el5.send_keys(WIFI_password)
time.sleep(2)
if (clickButton(reportFile, "next_button") == False):
    exit()

time.sleep(20)

'''

## Need to add step for remove purifier