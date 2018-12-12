import ctypes  # An included library with Python install.
import json
import time
import ctypes  # An included library with Python install.
import datetime
import os

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from subprocess import Popen

# Returns abs path relative to this file and not cwd


desired_caps = {'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName':'Samsung Galaxy S6',
                'app':'C:\\Users\\sli\\pycharmprojects\\appium framework\\DysonLink-ble-debug.apk',
                'appPackage': 'com.dyson.mobile.android.ble.weekly.debug',
                'appActivity': 'com.dyson.mobile.android.launch.LaunchActivity',
                'cloudEnvironmentAndroid':'integration',
                'noReset': 'true',
}

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)



#Get the information to locate the machine
with open('C:\\Users\\sli\\PycharmProjects\\appium framework\\config.json', 'r+') as configFile:
    config = json.load(configFile)
    machine_location= config['Machine Location']
    testResultFolder = config['testResultFolder']
    machine_serial = config['Machine Serial']

#print(machine_location)
#Preparelog
startTime = datetime.datetime.now().strftime("%I_%M_%S_%p_%B_%d_%Y")
reportPath = testResultFolder + '\\' + 'Reports'
if not os.path.exists(reportPath):
    os.makedirs(reportPath)
filename = 'Log ' + startTime + '.txt'
reportFile = open(reportPath + '\\' + filename, 'w')
reportFile.write('This log is for instant control of machine' + machine_serial + '\n')
reportFile.write('Log starts at ' + startTime + '\n')

## This is used to shake the devide for the SI server to set Region

#Mbox('Reminder', 'Set location and Environments, you have 10 seconds', 1)
#time.sleep(10)


for x in range(1,6):
    time.sleep(10)
    el1 = driver.find_element_by_id('location_textview')  # if find the machine is the correct location, if will click the buttons to enter setting
    if (el1.text == machine_location):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'oval_left_imageview')))
        el5 = driver.find_element_by_id('oval_left_imageview')
        el5.click()
        reportFile.write('Machine selected and setting entered\n')
        break
    else:
        #print(el1.text)
        if (x!=5):
            driver.swipe(900, 1500, 100, 1500)
        else: # quit after 5 times and retry
            reportFile.write('machine not found\n')
            exit()



#Mbox('Reminder', 'You should see the machine now', 1)


#Toggle on/off switch
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'power_toggle')))
el6 = driver.find_element_by_id('power_toggle')
time.sleep(3)
if el6.is_selected():
    el6.click()
time.sleep(3)
el6.click()
time.sleep(3)

#Setting Automode
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'auto_toggle')))
el13=driver.find_element_by_id('auto_toggle')
if el13.is_selected():
    el13.click()
time.sleep(3)
el13.click()
time.sleep(3)
Popen("C:\\Users\\sli\\PycharmProjects\\appium framework\\Labview Scripts\\Readings\\ReadAUTO\\ReadingAUTO.exe")
time.sleep(10)
with open('C:\\Users\\sli\\PycharmProjects\\appium framework\\Readings\\ReadingAUTO.json', 'r+') as configFile:
    config1 = json.load(configFile)
    AUTO_Mode= config1['Manual_Auto']
if AUTO_Mode == 'Auto':
    reportFile.write('AUTO is set properly\n')
time.sleep(2)
el13.click()
time.sleep(3)
#Changing Fan Level
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'fan_speed')))
el7=driver.find_element_by_id('fan_speed')
el7.click()
time.sleep(3)
#Mbox('Reminder', 'You should enter the fan settings', 1)
time.sleep(3)
#Set the speed
Popen("C:\\Users\\sli\\Desktop\\520 scripts\\TAB.bat")
#Mbox('Reminder', 'FANSPEED IS SET TO 10', 1)
Popen("C:\\Users\\sli\\PycharmProjects\\appium framework\\Labview Scripts\\Readings\\ReadFan\\ReadingFAN.exe")
time.sleep(10)
with open('C:\\Users\\sli\\PycharmProjects\\appium framework\\Readings\\ReadingFAN.json', 'r+') as configFile:
    config2 = json.load(configFile)
    FAN_SPEED= config2['Manual Speed']
if FAN_SPEED == '5':
    reportFile.write('FAN is set properly\n')

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'fan_speed_done_button')))
el9=driver.find_element_by_id('fan_speed_done_button')
el9.click()
#Mbox('Reminder', 'Fan settings should be done', 1)


#Timer settings

# to be continued


#driver.quit()from appium import webdriver

