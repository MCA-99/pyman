# Imports
import os
import platform
from multiprocessing import Process
from time import sleep

# Detect OS
platform_name = platform.system()

def clear_console():
    if platform_name == "Linux":
        os.system("clear")
    elif platform_name == "Windows":
        os.system("cls")

# Brain
def brain():
    while True:
        lungs()


def lungs():
    print("inhale")
    sleep(1.5)
    print("exhale")
    sleep(1.5)

def talk():
    print("aaaaa")

brain()
# time.sleep(1.5 - ((time.time() - starttime) % 1.5))