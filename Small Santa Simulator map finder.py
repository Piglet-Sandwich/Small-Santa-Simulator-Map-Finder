import keyboard as k
import pyautogui as pg
import time
from pyscreeze import ImageNotFoundException
import pydirectinput as pyd

print("Welcome!!! press \'p\' for help")
running = True
not_found = True
max_bulbs = 17
while running:
    if k.is_pressed('l') :
        print("L is pressed -- Searching")
        while not_found:
            time.sleep(0.1)
            pyd.press('r')
            time.sleep(0.01)
            pyd.press('tab')
            time.sleep(0.1)
            bulbs_found = 0
            try:
                print("ok")
                result = list(pg.locateAllOnScreen("bulb1.png", confidence=0.8))
                print("   -" + str(len(result)) + " bulbs found")
            except ImageNotFoundException:
                print("No Bulbs")
                result = []
            if len(result) <= max_bulbs and len(result) >= 12:
                print("Map with " + str(len(result)) + " bulbs found!")
                not_found = False
                pyd.press("escape")
                break
            else:
                print("reseting")
            if k.is_pressed("o"):
                print("O is pressed -- cancelling\n     -Hit k to reset")
                not_found = False

    if k.is_pressed("p"):
        print("P: this help menu")
        print("K: reset")
        print("L: search (or cancel search)")
        print("O: cancel search")
        print("H: enter max bulbs")
        print("J: break/exit program")

    if k.is_pressed('k'):
        print("K pressed -- Resetting")
        not_found = True
    
    if k.is_pressed('j'):
        print("J pressed -- Breaking")
        running = False
    
    if k.is_pressed('h'):
        print("H pressed -- Enter Max Bulbs (12+)")
        max_bulbs = int(input())
        print("Success -- Max bulbs set to " + str(max_bulbs))
    
    time.sleep(0.2)