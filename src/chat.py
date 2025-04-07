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

    for log in const.chatlog.find().sort("timestamp", 1):
        timestamp = log["timestamp"].strftime("%H:%M:%S")
        print(f"[{timestamp}] <{log['user']}: {log['message']}")

    while const.CHAT["active"]:
        os.system('clear')
        chatInput = input("> ")


        if not chatInput.startswith("/"):
            const.chatlog.insert_one({
                "user": usr,
                "timestamp": timestamp,
                "message": chatInput
            })
            
        if chatInput.lower() in ["/quit", "/q"]:
            const.CHAT["active"] = False
            os.system('clear')
            menu.menu()
        elif chatInput.lower() in ["/help"]:
            print("/quit or /q: Quit the current chat")
            print("/help: Prints all commands (including this one)")
            time.sleep(2)