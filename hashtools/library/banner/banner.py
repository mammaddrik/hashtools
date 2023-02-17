#::::: Library :::::
from hashtools.library.color.color import Color,color_banner

class Banner:
    "A Class To Print Different Banners."
    #::::: HashTools :::::
    hashtools_banner = (color_banner[0] + """ __ __   ____  _____ __ __  ______   ___    ___   _     _____
|  |  | /    |/ ___/|  |  ||      | /   \  /   \ | |   / ___/
|  |  ||  o  (   \_ |  |  ||      ||     ||     || |  (   \_ 
|  _  ||     |\__  ||  _  ||_|  |_||  O  ||  O  || |___\__  |
|  |  ||  _  |/  \ ||  |  |  |  |  |     ||     ||     /  \ |
|  |  ||  |  |\    ||  |  |  |  |  |     ||     ||     \    |
|__|__||__|__| \___||__|__|  |__|   \___/  \___/ |_____|\___|\n""" + Color.End + """
           {01}-Hash Cracker   {02}-Hash Generator
           {00}-Github         {99}-Exit""")
    
    #::::: HashCracker :::::
    hashcracker_banner = (color_banner[1] +"""                 _       ___               _             
  /\  /\__ _ ___| |__   / __\ __ __ _  ___| | _____ _ __ 
 / /_/ / _` / __| '_ \ / / | '__/ _` |/ __| |/ / _ \ '__|
/ __  / (_| \__ \ | | / /__| | | (_| | (__|   <  __/ |   
\/ /_/ \__,_|___/_| |_\____/_|  \__,_|\___|_|\_\___|_|\n""" + Color.End)

    #::::: HashGenerator  :::::
    hashgenerator_banner = (color_banner[2] +"""                 _       ___                          _              
  /\  /\__ _ ___| |__   / _ \___ _ __   ___ _ __ __ _| |_ ___  _ __  
 / /_/ / _` / __| '_ \ / /_\/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| 
/ __  / (_| \__ \ | | / /_ \  __/ | | |  __/ | | (_| | || (_) | |    
\/ /_/ \__,_|___/_| |_\____/\___|_| |_|\___|_|  \__,_|\__\___/|_|\n""" + Color.End)
    
    #::::: Github  :::::
    github_banner = (color_banner[3]+"""╔══════════════════════════════════════════╗
║   \033[1;37m["""+color_banner[4]+"""+\033[1;37m]hashtools."""+color_banner[3]+"""                          ║
║   \033[1;37m["""+color_banner[5]+"""+\033[1;37m]Tools for Hash Cracker & Generator."""+color_banner[3]+""" ║
╚══════════════════════════════════════════╝"""+Color.End)