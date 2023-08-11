class Settings:
    def __init__(self):
        self.__settings = {"pgo":{},"pcp":{}}#Password Generate Options,Password Check Policy
        self.readSettings()


    def saveSettings(self, AZ:bool, az:bool, nu:bool, sc:bool, length:int, lengthC:int, upperC:int, numbersC:int,
                     specialC:int, eabitC:int, strengthC:int):
        self.__settings["pgo"]["AZ"] = AZ
        self.__settings["pgo"]["az"] = az
        self.__settings["pgo"]["nu"] = nu
        self.__settings["pgo"]["sc"] = sc
        self.__settings["pgo"]["length"] = length
        self.__settings["pcp"]["length"] = lengthC
        self.__settings["pcp"]["upperC"] = upperC
        self.__settings["pcp"]["numbersC"] = numbersC
        self.__settings["pcp"]["specialC"] = specialC
        self.__settings["pcp"]["eabitC"] = eabitC
        self.__settings["pcp"]["strengthC"] = strengthC

    @property
    def getSettings(self) -> dict:
        print(self.__settings)
        return self.__settings

    def readSettings(self):
        pass

    def writeSettings(self):
        pass