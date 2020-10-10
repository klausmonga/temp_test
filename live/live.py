import time
import os


def Onstart():
    b = 0
    while 1:
        print(b)
        time.sleep(0.5)
        b = b + 1


def Oncreate():
    print(os.getpid())
    b = 0
    while 1:
        print(b)
        time.sleep(0.5)
        b = b + 1


if __name__ == "__main__":
    Oncreate()
