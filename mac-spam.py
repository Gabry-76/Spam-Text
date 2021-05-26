#<----------SPAM BOT---------->
import time
import pyperclip
import pyautogui

time.sleep(10)
f = open("import_spam","r")

for char in f:
    pyperclip.copy(char)
    pyautogui.hotkey('command', 'v', interval=0.02)
    pyautogui.typewrite("\n")
