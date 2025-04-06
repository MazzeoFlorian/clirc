#Login menu

import const
import hashlib
import menu
import os
import style
import time
import usrcreate

loginMenuCmds = (
    "login",
    "new user",
    "exit"
)



def loginMenu():
    while const.LOGINMENU["active"]:
        print(f"{style.bcolor.UNDERLINE}Login Menu{style.bcolor.ENDC}")
        print("")
        print("Select an option:")
        print("")
        print(f"{style.bcolor.OKCYAN}Login{style.bcolor.ENDC} to existing account.")
        print(f"Create a {style.bcolor.OKCYAN}new user{style.bcolor.ENDC} account.")
        print(f"{style.bcolor.OKCYAN}Exit{style.bcolor.ENDC} clirc.")

        menInp = input("> ")
        if menInp == loginMenuCmds[0]:
            usr_name = input("Enter user name: ")
            pwd = input("Enter password: ")

            auth = pwd.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            with open("credentials.txt", "r") as f:
                stored_usrn, stored_pwd = f.read().split("\n")
            f.close()

            if usr_name == stored_usrn and auth_hash == stored_pwd:
                print("")
                print(f"{style.bcolor.OKGREEN}Login successful!{style.bcolor.ENDC}")
                time.sleep(1)
                os.system('clear')
                const.MENU["active"] = True
                const.LOGINMENU["active"] = False
                menu.menu()
            else:
                print("")
                print(f"{style.bcolor.FAIL}Credentials not correct, try again.{style.bcolor.ENDC}")
                print("")
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
            print(f"{style.bcolor.FAIL}Wrong or unknown input.{style.bcolor.ENDC}")
            time.sleep(1)

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
