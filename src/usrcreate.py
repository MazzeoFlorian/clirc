#User creation script
import const
import getpass
import hashlib
import loginmenu
import os
import pymongo
import style
import time

def userCreation():
    while const.USRCREATE["active"]:
        print(f"{style.bcolor.UNDERLINE}{style.bcolor.OKCYAN}Account Creation{style.bcolor.ENDC}")
        print("")
        usr_name = input("Enter your user name: ")
        pwd = getpass.getpass("Enter your password: ")
        conf_pwd = getpass.getpass("Confirm your password: ")

        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1= hashlib.md5(enc).hexdigest()
        
            accountData = { "user": usr_name, "password_hash": hash1}
            const.usrdata.insert_one(accountData)

            print("")
            print(f"{style.bcolor.OKGREEN}Account successfully created!{style.bcolor.ENDC}")
            time.sleep(1)
            print("")
            print("Redirecting...")
            os.system('clear')
            const.USRCREATE["active"] = False
            const.LOGINMENU["active"] = True
            loginmenu.loginMenu()
        else:
            print("")
            print(f"{style.bcolor.FAIL} Passwords are not matching, please try again!")

