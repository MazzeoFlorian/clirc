##Chat module
import const
from datetime import datetime
import menu
import os
import pymongo
import time

timestamp = datetime.now().strftime('%H:%M:S')

def chatLoop():

    usr = const.CURRENT_USER

    while const.CHAT["active"]:
        os.system('clear')

        if os.path.exists("log.txt"):
            with open ("log.txt", "r") as logr:
                print(logr.read())

        chatInput = input("> ")

        if not chatInput.startswith("/"):
            with open("log.txt", "a") as logw:
                logw.write(f"[{timestamp}] <{usr}>: {chatInput}\n")
            
        if chatInput.lower() in ["/quit", "/q"]:
            const.CHAT["active"] = False
            os.system('clear')
            menu.menu()
        elif chatInput.lower() in ["/help"]:
            print("/quit or /q: Quit the current chat")
            print("/help: Prints all commands (including this one)")
            time.sleep(2)