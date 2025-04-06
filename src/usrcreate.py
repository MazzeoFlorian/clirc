#User creation script
import const
import hashlib
import os
import style
import time
import loginmenu

def userCreation():
    while const.USRCREATE["active"]:
        print(f"{style.bcolor.UNDERLINE}{style.bcolor.OKCYAN}Account Creation{style.bcolor.ENDC}")
        print("")
        usr_name = input("Enter your user name: ")
        pwd = input("Enter your password: ")
        conf_pwd = input("Confirm your password: ")

        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1= hashlib.md5(enc).hexdigest()
        
            with open("credentials.txt", "w") as f:
                f.write(usr_name + "\n")
                f.write(hash1)
            f.close()
            print("")
            print(f"{style.bcolor.OKGREEN}Account successfully created!{style.bcolor.ENDC}")
            time.sleep(1)
            os.system('clear')
            const.USRCREATE["active"] = False
            const.LOGINMENU["active"] = True
            loginmenu.loginMenu()
        else:
            print("")
            print(f"{style.bcolor.FAIL} Passwords are not matching, please try again!")

