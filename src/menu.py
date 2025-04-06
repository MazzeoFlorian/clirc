import const
import chat
import loginmenu
import os
import style
import time

#Menu tuple
menuCmds = (
    "new",
    "options",
    "logout"
)

# Menu function

def logout():
    time.sleep(1)
    os.system('clear')
    const.MENU["active"] = False
    const.LOGINMENU["active"] = True
    loginmenu.loginMenu()

def menu():
    while const.MENU["active"]:
        print(f"{style.bcolor.UNDERLINE}Main Menu{style.bcolor.ENDC}")
        print("")
        print("Select an option:")
        print("")
        print(f"Open {style.bcolor.OKCYAN}new{style.bcolor.ENDC} chat")
        print(f"{style.bcolor.OKCYAN}Options{style.bcolor.ENDC} (NYI)")
        print(f"{style.bcolor.OKCYAN}Logout{style.bcolor.ENDC} clirc")

        #Input options
        menInp = input("> ")
        if menInp == menuCmds[0]:
            time.sleep(1)
            os.system('clear')
            const.CHAT["active"] = True
            chat.chatLoop()
        elif menInp == menuCmds[1]:
            print(f"{style.bcolor.WARNING}Not yet implemented.{style.bcolor.ENDC}")
            time.sleep(1)
            os.system('clear')
        elif menInp == menuCmds[2]:
            logout()
        else:
            print("")
            print(f"{style.bcolor.FAIL}Wrong or unknown input.{style.bcolor.ENDC}")
            time.sleep(1)
            os.system('clear')