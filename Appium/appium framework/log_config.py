import json
import os


class LogConfig:
    def __init__(self):
        configFileName = 'c:\\date_config.json'
        if (os.path.isfile(configFileName) == False):
            configFileName = 'date_config.json'
        with open(configFileName, 'r') as outFile:
            config = json.load(outFile)
            datePath = config['datePath']
            self.logLevel = config['logLevel']
            self.deleteLog = config['deleteLog']
        outFile.close()

        self.fullFileName = datePath + '\\framework_log.txt'
