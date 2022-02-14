#<---------- DON'T TOUCH ---------->
print('[Debug] Start Spamming ✔')
import time
import json
from pyperclip import copy
from pyautogui import hotkey, typewrite

file = open('settings.json')
time.sleep(8)
counter = 0;

try:
  data = json.load(file)
except:
    print(f'[Debug] Can\'t Open settings.json, using Default Settings ❌')

try:
  message = data['message']
except:
  message = 'Nothing'
  
try:
  messageCount = data['messageCount']
except:
  messageCount = 1

file.close()

while True:
    if (counter < int(messageCount)):
        copy(f'{message} - Tool By Gabry_76#0039')
        hotkey('ctrl', 'v', interval=0.0)
        typewrite('\n')
        counter = counter + 1
    elif (counter == int(messageCount)):
        print('[Debug] Finished Spamming ✔')
        break