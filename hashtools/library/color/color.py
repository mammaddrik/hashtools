import random

#::::: Color :::::
class Color:
    "A Class To Specify Colors."
    End = "\033[1;37m"  #white  
    BRed = "\033[1;31m"
    BGreen = "\033[1;32m"
    BYellow = "\033[1;33m"
    BBlue = "\033[1;34m"
    BPurple = "\033[1;35m"
    BCyan = "\033[1;36m"

color_banner = [Color.BRed,Color.BGreen,Color.BYellow,Color.BBlue,Color.BPurple,Color.BCyan]
random.shuffle(color_banner)