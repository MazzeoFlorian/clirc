import pymongo
#Constants

MAIN = True
CHAT = {"active": True}
MENU = {"active": True}
LOGINMENU = {"active": True}
USRCREATE = {"active": True}

#Version number
VERSION = "0.2.2.a"

#Database
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["clirc-db"]
usrdata = database["users"]
chatlog = database["chatlog"]

#user
CURRENT_USER = None
