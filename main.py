import pyautogui
import time
time.sleep(5)
x=4000
numbers=[3900, 3800, 3700, 3600, 3500, 2300, 3300, 3200, 3100, 3000, 2900, 2800, 2700]
while x>0:
    pyautogui.leftClick(1862, 306, 0.4)
    pyautogui.leftClick(1759, 441, 0.4)
    x-=1
    if x in numbers:
        pyautogui.leftClick(96, 62, 0.3)
        time.sleep(5)