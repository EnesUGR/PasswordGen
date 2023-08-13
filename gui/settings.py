import winreg

class Settings:
    def __init__(self,appname:str):
        self.__settings = {"pgo":{},"pcp":{}} #Password Generate Options,Password Check Policy
        self.__appname = appname
        self.__readSettings()


    def saveSettings(self, AZ:bool, az_:bool, nu:bool, sc:bool, length:int, lengthC:int, upperC:int, numbersC:int,
                     specialC:int, eabitC:int, strengthC:float):
        self.__settings["pgo"]["AZ"] = AZ
        self.__settings["pgo"]["az_"] = az_
        self.__settings["pgo"]["nu"] = nu
        self.__settings["pgo"]["sc"] = sc
        self.__settings["pgo"]["length"] = length
        self.__settings["pcp"]["length"] = lengthC
        self.__settings["pcp"]["upperC"] = upperC
        self.__settings["pcp"]["numbersC"] = numbersC
        self.__settings["pcp"]["specialC"] = specialC
        self.__settings["pcp"]["eabitC"] = eabitC
        self.__settings["pcp"]["strengthC"] = strengthC
        self.__writeSettings()


    @property
    def getSettings(self) -> dict:
        return self.__settings

    @property
    def isEmpty(self) -> bool:
        return len(self.__settings['pgo']) == 0 or len(self.__settings['pcp']) == 0


    def __readSettings(self):
        print("READ_SETTINGS")
        soft = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"SOFTWARE\\")
        pgo = winreg.OpenKeyEx(soft,r"{0}\\pgo".format(self.__appname),0,winreg.KEY_READ)
        pcp = winreg.OpenKeyEx(soft,r"{0}\\pcp".format(self.__appname),0,winreg.KEY_QUERY_VALUE)
        i = 0
        while True:
            try:
                y = winreg.EnumValue(pcp,i) #6 pieces
                self.__settings["pcp"][y[0]] = int(y[1]) if y[1].find(".") == -1 else float(y[1])

                x = winreg.EnumValue(pgo,i) #5 pieces
                self.__settings["pgo"][x[0]] = bool(x[1]) if x[1] <= 1 else x[1]

                i += 1
            except WindowsError:
                break


    def __writeSettings(self):
        print("WRITE_SETTINGS")
        soft = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"SOFTWARE\\")
        pgo = winreg.OpenKeyEx(soft,r"{0}\\pgo".format(self.__appname),0,winreg.KEY_SET_VALUE)
        pcp = winreg.OpenKeyEx(soft,r"{0}\\pcp".format(self.__appname),0,winreg.KEY_SET_VALUE)

        for k,v in self.__settings["pgo"].items():
            winreg.SetValueEx(pgo,k,0,winreg.REG_DWORD,v)
        for k,v in self.__settings["pcp"].items():
            winreg.SetValueEx(pcp,k,0,winreg.REG_SZ,str(v))

        winreg.CloseKey(soft)
        winreg.CloseKey(pgo)
        winreg.CloseKey(pcp)


    @staticmethod
    def first_create(appname:str,version:str) -> None:
        loc = winreg.HKEY_CURRENT_USER
        soft = winreg.OpenKeyEx(loc,r"SOFTWARE\\")
        mysoft_pgo = winreg.CreateKey(soft,r"{0}\\pgo".format(appname))
        mysoft_pcp = winreg.CreateKey(soft,r"{0}\\pcp".format(appname))

        winreg.CloseKey(soft)
        winreg.CloseKey(mysoft_pgo)
        winreg.CloseKey(mysoft_pcp)