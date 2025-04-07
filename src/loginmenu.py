#Login menu

import const
import getpass
import hashlib
import menu
import os
import pymongo
import style
import time
import usrcreate

loginMenuCmds = (
    "login",
    "create",
    "exit"
    )

def loginMenu():
    while const.LOGINMENU["active"]:
        print(f"{style.bcolor.UNDERLINE}Login Menu{style.bcolor.ENDC}")
        print("")
        print("Select an option:")
        print("")
        print(f"{style.bcolor.OKCYAN}Login{style.bcolor.ENDC} to existing account.")
        print(f"{style.bcolor.OKCYAN}Create{style.bcolor.ENDC} a new account.")
        print(f"{style.bcolor.OKCYAN}Exit{style.bcolor.ENDC} clirc.")

        menInp = input("> ")
        if menInp == loginMenuCmds[0]:
            print("")
            usr_name = input("Enter user name: ")
            pwd = getpass.getpass("Enter password: ")

            auth = pwd.encode()
            auth_hash = hashlib.md5(auth).hexdigest()

            user = const.usrdata.find_one({"user": usr_name, "password_hash": auth_hash })

            if user:
                print("")
                print(f"{style.bcolor.OKGREEN}Login successful!{style.bcolor.ENDC}")
                time.sleep(1)
                os.system('clear')
                const.MENU["active"] = True
                const.LOGINMENU["active"] = False

                #Save logged in user globally
                const.CURRENT_USER = usr_name

                menu.menu()
            else:
                print("")
                print(f"{style.bcolor.FAIL}Credentials not correct, try again.{style.bcolor.ENDC}")
                print("")
                os.system("clear")
        elif menInp == loginMenuCmds[1]:
            os.system("clear")
            usrcreate.userCreation()
        elif menInp == loginMenuCmds[2]:
            os.system('clear')
            print(f"{style.bcolor.BOLD}Exiting clirc.{style.bcolor.ENDC}")
            time.sleep(1)
            const.LOGINMENU["active"] = False
            const.MAIN = False
            os.system('clear')
        else:
            print("")
            print(f"{style.bcolor.FAIL}Wrong or unknown input.{style.bcolor.ENDC}")
            print("")
            time.sleep(1)
            os.system("clear")

def startUp():
    os.system('clear')
    print(f"{style.bcolor.BOLD}clirc {const.VERSION}{style.bcolor.ENDC}")
    time.sleep(1)
    print("by Florian Mazzeo (2025 - )")
    print("")
    time.sleep(1)
    print(f"Source available on: {style.bcolor.UNDERLINE}https://github.com/MazzeoFlorian/clirc{style.bcolor.ENDC}")
    time.sleep(1)
    os.system("clear")
    loginMenu()
