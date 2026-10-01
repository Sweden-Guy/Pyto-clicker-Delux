import pyautogui
import keyboard

ac = 1

while True:
    x, y = pyautogui.position()

    if keyboard.is_pressed('q'):
        if ac == 1:
            #pyautogui.click(x, y)
            ac = 0
        elif ac == 0:
            ac = 1

    if ac == 0:
        pyautogui.click(x, y)