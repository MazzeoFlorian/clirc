##Chat module
import const
import os
from datetime import datetime
import menu

timestamp = datetime.now().strftime('%H:%M:S')

def chatLoop():
    while const.CHAT["active"]:
        os.system('clear')

        if os.path.exists("log.txt"):
            with open ("log.txt", "r") as logr:
                print(logr.read())

        chatInput = input("> ")
        timestamp = datetime.now().strftime('%H:%H:%S')

        with open("log.txt", "a") as logw:
            logw.write(f"[{timestamp}] <User:>: {chatInput}\n")
            
        if chatInput.lower() == "logout":
            const.CHAT["active"] = False
            os.system('clear')
            menu.menu()