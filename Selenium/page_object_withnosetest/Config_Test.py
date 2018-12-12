import json


class TestAutomationConfig:

    def __init__(self):
        configFileName = 'Config_Data.json'
        with open(configFileName, 'r') as outFile:
            config = json.load(outFile) #load json content
            self.browser = config['TestBrowser']
            self.testserver = config['TestServer']
            self.serverlist = config['Server Address']
            for row in self.serverlist:
                if row['Server'] ==self.testserver:
                    self.login = row['Login Page']
                    self.mainpage = row['Main Page']
                    self.maindashboard = row['MainDashboard']
            self.languageselector = config['languageselector']
            self.language = config['Language']
            self.user = config["username"]
            self.pwd = config['password']


            self.Key = config['Keys']
            self.submit = self.Key['submit']
            self.home = self.Key['home']
            self.settings = self.Key['settings']
            self.statistics = self.Key['statistics']
            self.dashboard = self.Key['dashboard']
            self.announcement = self.Key['announcement']
            self.loginarrow=self.Key['loginbutton']
            self.loginbutton= self.Key['logintag']
            self.username = self.Key["username"]
            self.password = self.Key['password']
            self.englan = self.Key['English']
            self.chilan = self.Key['Chinese']
            self.ruslan = self.Key['Russian']

            self.English = config['English']
            self.English_Home = self.English['home']
            self.English_Dashboard = self.English['dashboard']
            self.English_Settings = self.English['settings']
            self.English_Statistics = self.English['statistics']
            self.English_Announcement = self.English['announcement']

            self.Chinese = config['Chinese']
            self.Chinese_Home = self.Chinese['home']
            self.Chinese_Dashboard = self.Chinese['dashboard']
            self.Chinese_Settings = self.Chinese['settings']
            self.Chinese_Statistics = self.Chinese['statistics']
            self.Chinese_Announcement = self.Chinese['announcement']

            self.Russian = config['Russian']
            self.Russian_Home = self.Russian['home']
            self.Russian_Dashboard = self.Russian['dashboard']
            self.Russian_Settings = self.Russian['settings']
            self.Russian_Statistics = self.Russian['statistics']
            self.Russian_Announcement = self.Russian['announcement']

            

        outFile.close()


TestAutomationConfig()