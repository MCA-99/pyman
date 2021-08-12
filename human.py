# Imports
import os
import platform
from multiprocessing import Process, Manager, managers
from time import sleep

# Global variables
manager = Manager()
shared_var = manager.dict()

# Detect OS
platform_name = platform.system()


def clear_console():
    if platform_name == "Linux":
        os.system("clear")
    elif platform_name == "Windows":
        os.system("cls")


def brain():
    proc_lungs = Process(target=lungs)
    proc_lungs.start()

    while True:
        thought = input("Write an action: ")
        if thought == "lungs":
            print("Lungs status: " + shared_var["lung_status"])
        elif thought == "talk":
            talk()
        elif thought == "kill":
            proc_lungs.terminate()


def lungs():
    while True:
        shared_var["lung_status"] = "inhale"
        # print("lungs status ==> " + lungs_status)
        sleep(1.5)
        shared_var["lung_status"] = "exhale"
        # print("lungs status ==> " + lungs_status)
        sleep(1.5)


def talk():
    if shared_var["lung_status"] == "exhale":
        print("aaaaa")
    else:
        sleep(1.5)
        talk()


brain()
