import time
import sys

#::::: Slowprint :::::
def slowprint(s):
    "A Function To Print A Sentence Word For Word."
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)