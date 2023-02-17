import os

#::::: clearScreen :::::
def clearScr():
    "A Function To Clean Up The Command Prompt or Terminal."
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")