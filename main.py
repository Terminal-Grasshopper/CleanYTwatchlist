import random
import pyautogui
import time
time.sleep(5)

while True:
    pyautogui.leftClick(1845, 285, 0.5)
    pyautogui.leftClick(1700, 417, 0.5)
    if random.randint(0, 100) < 3:
        pyautogui.leftClick(82, 44, 0.3)
        time.sleep(5)
