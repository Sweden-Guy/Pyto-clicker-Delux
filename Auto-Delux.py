import pyautogui
import keyboard
import time

pyautogui.PAUSE = 0

def Clicks(x):
    if x <= 0:
        return 0
    return 1 / x

while True:
    ac = 1  
    print("\n--- Auto Clicker Deluxe ---")
    print("What CPS do you want?")
    
    try:
        CPS = float(input())
    except ValueError:
        print("Please enter a valid number.")
        continue
        
    print(f"Ok, {CPS} is selected")
    print("If you want to change CPS press F7")
    print("Press F6 to toggle the autoclicker ON/OFF.")
    
    delay = Clicks(CPS)
    restart = False

    while not restart:
        # Toggle ON/OFF med F6
        if keyboard.is_pressed('f6'):
            if ac == 1:
                ac = 0
                print("Autoclicker ON")
            else:
                ac = 1
                print("Autoclicker OFF")
            
            while keyboard.is_pressed('f6'):
                time.sleep(0.05)

        if keyboard.is_pressed('f7'):
            print("Restarting... Choose new CPS.")
            restart = True

            while keyboard.is_pressed('f7'):
                time.sleep(0.05)
            break 

        if ac == 0:
            pyautogui.click()
            if delay > 0:
                time.sleep(delay)
