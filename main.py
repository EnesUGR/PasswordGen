from gui.home import run_ui
from gui.settings import Settings


APPNAME = "PasswordGen"
VERSION = "1.1.1"


if __name__ == '__main__':
    Settings.first_create(APPNAME,VERSION)
    run_ui(APPNAME,VERSION)
