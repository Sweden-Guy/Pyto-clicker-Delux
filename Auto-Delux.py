import pyautogui
import keyboard
import time

ac = 1

print("Auto Clicker Delux")
print("What CPS do you want?")
CPS = float(input())
print(f"Ok, {CPS} is seleced")

def Clicks(x):
    if x == 0:
        return "Needs to be a posetiv number!"
    return 1 / x 

while True:
    x, y = pyautogui.position()

    if keyboard.is_pressed('q'):
        if ac == 1:
            ac = 0
            print("Autoclicker ON")
        elif ac == 0:
            ac = 1
            print("Autoclicker OFF")
    #keyboard.wait('q')
    if ac == 0:
        pyautogui.click(x, y)
        time.sleep(Clicks(CPS))