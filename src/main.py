#clirc main file

import commands
import const
import loginmenu
import time
import style
import os
import pymongo

def main():
    while const.MAIN == True:
        loginmenu.startUp()

main()