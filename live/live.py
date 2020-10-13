import time
import os
import json

def Onstart():
    b = 0
    while 1:
        print(b)
        time.sleep(0.5)
        b = b + 2


def Oncreate():
    with open('prod_pid.bin', 'w') as outfile:
        json.dump({"pid": os.getpid()}, outfile)
    Onstart()

if __name__ == "__main__":
    Oncreate()
