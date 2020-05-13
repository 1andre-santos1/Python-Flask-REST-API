import configparser

class configuration:

    configFile = "config.ini"
    config = ""

    def __init__(self, fileName):
        self.configFile = fileName
        self.config = configparser.ConfigParser()
        self.config.read(fileName)


    def readConfigFile(self, fileName):
        self.config.clear()
        self.configFile = fileName
        self.config.read(self.configFile)


    def get(self, section, prop):
        return self.config[section][prop]