from pymouse import PyMouse
import pyautogui
import keyboard  # using module keyboard

ac =1
while True:  # making a loop
    pyautogui.position()
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            m.click(x,y,1) #the third argument "1" represents the mouse button
           
    except:
        break  # if user pressed a key other than the given key the loop will break


pyautogui.position()


m = PyMouse()
m.position() #gets mouse current position coordinates
m.move(x,y)
m.click(x,y) #the third argument "1" represents the mouse button
m.press(x,y) #mouse button press
m.release(x,y) #mouse button release

