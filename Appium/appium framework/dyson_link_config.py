import json


class DysonLinkConfig:
    def __init__(self):
        configFileName = 'C:\\Users\\sli\\PycharmProjects\\appium framework\\config.json'
        with open(configFileName, 'r') as outFile:
            config = json.load(outFile)
            self.machine_serial = config['Machine Serial']
            self.testResultFolder = config['testResultFolder']
            self.username = config['User Name']
            self.password = config['Password']
            self.WIFI_password = config['WIFI password']
            self.prefix = config['Machine Prefix']
            self.machine_location = config['Machine Location']
        outFile.close()

class DysonLinkButtonConfig:
    def __init__(self):
        configFileName = 'C:\\Temp\\reading.json'
        with open(configFileName, 'r') as outFile:
            config = json.load(outFile)
            self.power = config["System State"]
            self.fanspeed = config["Manual Speed"]
            self.auto = config["Manual_Auto"]
            self.front = config["Back_Front"]
            self.status = config["Normal_DND"]
            self.osc = config["Oscillation"]
            self.timer = config["Sleep Timer"]
        outFile.close()