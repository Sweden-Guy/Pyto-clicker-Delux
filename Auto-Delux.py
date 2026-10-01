import pyautogui
import keyboard
import time

ac = 1

print("Auto Clicker Delux")
print("What CPS do you want?")
CPS = input()
print(f"Ok, {CPS} is seleced")

while True:
    x, y = pyautogui.position()

    if keyboard.is_pressed('q'):
        if ac == 1:
            ac = 0
            print("Autoclicker ON")
        elif ac == 0:q
            ac = 1
            print("Autocqlicker OFF")

        #keyboard.wait('q')

    if ac == 0:
        pyautogui.click(x, y)
        time.sleep(0.01)