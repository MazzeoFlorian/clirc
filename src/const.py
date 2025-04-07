import pymongo
#Constants

MAIN = True
CHAT = {"active": True}
MENU = {"active": True}
LOGINMENU = {"active": True}
USRCREATE = {"active": True}

#Version number
VERSION = "0.2.1"

#Database
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["clirc-db"]
usrdata = database["users"]

#user
CURRENT_USER = None
