import tkinter as tk
import keyboard as k
import pydirectinput as pyd
import pyautogui as pg
import time
from pyscreeze import ImageNotFoundException

searching = False
max_bulbs = 17

def start_search():
    global searching
    searching = True
    status_label.config(text="Searching...")
    search_step()

def cancel_search():
    global searching
    searching = False
    status_label.config(text="Cancelled")

def search_step():
    global searching
    if not searching:
        return

    pyd.press('r')
    time.sleep(0.01)
    pyd.press('tab')
    time.sleep(0.1)

    try:
        result = list(pg.locateAllOnScreen(r"C:\Users\samee\Downloads\Code\Microsoft Studios\Game Hacking\bulb1.png", confidence=0.8))
        status_label.config(text=f"{len(result)} bulbs found")
    except ImageNotFoundException:
        status_label.config(text="No bulbs found")
        result = []

    if 12 <= len(result) <= max_bulbs:
        status_label.config(text=f"Found {len(result)} bulbs!")
        pyd.press("escape")
        searching = False
        return

    root.after(50, search_step)

"""
max_bulbs = 17
def search():
    status_label.config(text="Searching")
    while True:
        time.sleep(0.1)
        pyd.press('r')
        time.sleep(0.01)
        pyd.press('tab')
        time.sleep(0.1)
        bulbs_found = 0
        try:
            result = list(pg.locateAllOnScreen("bulb1.png", confidence=0.8))
            print("   -" + str(len(result)) + " bulbs found")
        except ImageNotFoundException:
            print("No Bulbs")
            result = []
        if len(result) <= max_bulbs and len(result) >= 12:
            print("Map with " + str(len(result)) + " bulbs found!")
            pyd.press("escape")
            break
        else:
            print("reseting")
        if k.is_pressed("o"):
            status_label.config("O is pressed -- cancelling")
            break
"""

def show_value(val):
    global max_bulbs
    max_bulbs = int(val)
    slider_value_label.config(text=f"Looking for at most {val} pickups")

root = tk.Tk()
root.title("SSS map finder")
root.attributes("-topmost", True)

frame = tk.Frame(root, padx=10, pady=10)
frame.grid()

title_label = tk.Label(frame, text="SSS map finder")
title_label.grid(column=0, row=0)

status_label = tk.Label(frame, text="Welcome!")
status_label.grid(column=0, row=3)

slider_value_label = tk.Label(frame, text="Looking for at most 17 pickups")
slider_value_label.grid(column=0, row=2)

tk.Button(frame, text="Quit", command=root.destroy).grid(column=0, row=5)
tk.Button(frame, text="Search", command=start_search).grid(column=0, row=1)
tk.Button(frame, text="Cancel Search", command=cancel_search).grid(column=1, row=1)

my_slider = tk.Scale(frame,from_=12, to=24, orient=tk.HORIZONTAL, command=show_value)
my_slider.grid(column=1, row=2)
my_slider.set(17)

root.mainloop()

