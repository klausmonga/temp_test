import time
import os
import json

def Onstart():
    b = 0
    while 1:
        print(b)
        time.sleep(1)
        b = b + 1
        os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch1/temp -m " + str(b))


def Oncreate():
    with open('prod_pid.bin', 'w') as outfile:
        json.dump({"pid": os.getpid()}, outfile)
    Onstart()

if __name__ == "__main__":
    Oncreate()
