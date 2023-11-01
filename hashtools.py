#!/usr/bin/env python
#  __ __   ____  _____ __ __  ______   ___    ___   _     _____
# |  |  | /    |/ ___/|  |  ||      | /   \  /   \ | |   / ___/
# |  |  ||  o  (   \_ |  |  ||      ||     ||     || |  (   \_ 
# |  _  ||     |\__  ||  _  ||_|  |_||  O  ||  O  || |___\__  |
# |  |  ||  _  |/  \ ||  |  |  |  |  |     ||     ||     /  \ |
# |  |  ||  |  |\    ||  |  |  |  |  |     ||     ||     \    |
# |__|__||__|__| \___||__|__|  |__|   \___/  \___/ |_____|\___|
#
#              Tools for Hash Cracker & Generator   
#                      Github: mammaddrik            

#::::: Library :::::
from hashtools.library.clearscreen.clearscr import clearScr
from hashtools.library.banner.banner import Banner
from hashtools.library.slowprint.slowprint import slowprint
from hashtools.library.color.color import Color,color_banner

#::::: Default Library :::::
from datetime import datetime
import webbrowser
import os
import sys
import time

try:
    import hashlib
except:
    os.system("pip3 install -r requirements.txt")

#::::: Again :::::
def again():
    "A Function To Ask The User To Restart The Program."
    hahs_again = input(Color.BCyan +"\nDo you want to continue? [Y/n]"+ color_banner[0]+"\nλ "+Color.End)
    if (hahs_again.upper() == "Y" or hahs_again == ""):
        clearScr()
        hashtools()
    elif (hahs_again.upper() == "N"):
        print("\n    Goodbye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()
    else:
        clearScr()
        hashtools()

#::::: Main Menu :::::
def hashtools():
    "The Main Function Of Hashtools"
    clearScr()
    time.sleep(0.4)
    print(Banner.hashtools_banner)
    choice = input(color_banner[0]+"λ "+Color.End)
    
    #::::: HashCracker :::::
    if (choice == "01" or choice == "1"):
        clearScr()
        time.sleep(0.4)
        print(Banner.hashcracker_banner)
        Hash = input("Enter the hash: ").lower()
        if len(Hash) == 32:
            hashvalue = "md5"
            slowprint("Hash Function:"+ Color.BYellow +" MD5")
        elif len(Hash) == 40:
            hashvalue = "sha1"
            slowprint("Hash Function:"+ Color.BYellow +" SHA1")
        elif len(Hash) == 64:
            hashvalue = "sha256"
            slowprint("Hash Function:"+ Color.BYellow +" SHA256")
        elif len(Hash) == 96:
            hashvalue = "sha384"
            slowprint("Hash Function:"+ Color.BYellow +" SHA384")
        elif len(Hash) == 128:
            hashvalue = "sha512"
            slowprint("Hash Function:"+ Color.BYellow +" SHA512")
        else:
            slowprint(Color.BRed +"Hash Function:"+ Color.BYellow +" Unknown")
            again()
        
        pwfile = input(Color.End+"Enter the password file name: ")
        
        try:
            with open(pwfile, "r") as f:
                filesize = os.path.getsize((pwfile))
                if filesize == 0:
                    slowprint(Color.BRed +"File is Empty.")
                    again()
        except FileNotFoundError:
                slowprint(Color.BRed +"File Not Found.")
                again()
        
        with open(pwfile, "r") as f:
            counter = 1
            t1 = datetime.now()
            for password in f:
                h = hashlib.new(hashvalue)
                setpass = bytes(password.strip(), "utf-8")
                h.update(setpass)
                hashedguess = h.hexdigest()
                print(f"Password number {counter}: {password.strip()}")
                counter += 1
                if Hash == hashedguess:
                    print(Color.BGreen+f"\nPassword: {password}")
                    t2 = datetime.now()
                    t3 = t2 - t1
                    time.sleep(0.4)
                    print(Color.BPurple+f"\nFinishing Time: {t3}")
                    again()
            else:
                time.sleep(0.4)
                slowprint(Color.BRed+"\nPassword Not Found :("+Color.End)
                again()

    #::::: Hash Generator :::::
    elif (choice == "02" or choice == "2"):
        clearScr()
        time.sleep(0.4)
        print(Banner.hashgenerator_banner)
        password = input("Enter the password: ")
        hashvalue = input("""\n{1}--MD5     {2}--SHA1    {3}--SHA224
{4}--SHA256  {5}--SHA384  {6}--SHA512
Enter the Algorithms: """)
        if(hashvalue == "01" or hashvalue == "1"):
            hashvalue = "MD5"
        elif(hashvalue == "02" or hashvalue == "2"):
            hashvalue = "SHA1"
        elif(hashvalue == "03" or hashvalue == "3"):
            hashvalue = "SHA224"
        elif(hashvalue == "04" or hashvalue == "4"):
            hashvalue = "SHA256"
        elif(hashvalue == "05" or hashvalue == "5"):
            hashvalue = "SHA384"
        elif(hashvalue == "06" or hashvalue == "6"):
            hashvalue = "SHA512"
        else:
            slowprint(Color.BRed +"Enter the Available Algorithm.")
            again()

        for i in range(1):
            setpass = bytes(password, "utf-8")
            h = hashlib.new(hashvalue)
            h.update(setpass)
            Hash = h.hexdigest()
            time.sleep(0.4)
            print(f"\n{hashvalue} Hash: {Hash}")
            again()
            
    #::::: Github :::::
    elif (choice == "00" or choice == "0"):
        clearScr()
        time.sleep(0.4)
        print(Banner.github_banner)
        url = "https://github.com/mammaddrik"
        webbrowser.open(url)
        again()
        
    #::::: Exit :::::
    elif (choice == "99"):
        print("\nGoodBye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()

    else:
        print(Color.BRed +"\nIt is wronge.")
        again()
try:
    hashtools()
    again()
except KeyboardInterrupt:
    slowprint(Color.BRed +"Finishing up..."+Color.End)
    time.sleep(0.4)
    clearScr()
