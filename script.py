import os
import subprocess
import time
import threading 

from pynput.keyboard import Key, Controller

keyboard = Controller()

def open_exe():
    os.system('"custdata.txt.sda.exe"')

def print_text(print_once):
    if print_once == 1:
        time.sleep(5)
        keyboard.type('MTZrtypu019')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print_once += 1

t1 = threading.Thread(target=print_text, args = (1,))
t2 = threading.Thread(target=open_exe)

t1.start() 
t2.start()

# subprocess.call(["E:/JE_TEST/custdata.txt.sda.exe"])



# keyboard.type('Nitratine')

