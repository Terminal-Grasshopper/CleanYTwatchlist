import random
import pyautogui
import time



pyautogui.alert(text="The script will wait 3 seconds after you click on \"OK\" for you to hover over the three dots so it can save the coordinates", title="YT Watch later remover")
time.sleep(3)
x1, y1 = pyautogui.position()
pyautogui.alert(text="Coordinates saved", title="YT Watch later remover")

pyautogui.alert(text="The script will wait 3 seconds after you click on \"OK\" for you to hover over \"Remove from Watch later\" so it can save the coordinates", title="YT Watch later remover")
time.sleep(3)
x2, y2 = pyautogui.position()
pyautogui.alert(text="Coordinates saved", title="YT Watch later remover")

remove_num = int(pyautogui.prompt(text='How many videos do you want removed?', title="YT Watch later remover"))
confirmation = pyautogui.confirm(text="The script will start in 5 seconds, you click \"Cancel\" to cancel this operation.", title="YT Watch later remover", buttons=["Continue", "Cancel"])
cancel="Cancel"
if confirmation == cancel:
    quit()
else:
    time.sleep(5)
    while remove_num > 0:
        pyautogui.leftClick(x1, y1, 0.5)
        pyautogui.leftClick(x2, y2, 0.5)
        remove_num -= 1
        if random.randint(0, 100) < 3:
            pyautogui.hotkey('ctrl' + 'f5')
            time.sleep(5)