import os
import datetime, time
from time import sleep


def clear():
    os.system("clear")

def newScene(x):
    sleep(x)
    clear()

def loadingAnimation(cycles):
    clear()
    for loop in range(cycles):
        print("loading.")
        newScene(.5)
        print("loading..")
        newScene(.5)
        print("loading...")
        newScene(.5)

loadingAnimation(3)
