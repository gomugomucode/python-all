# position_check.py
import pyautogui
import time

print("Move your mouse... position will be shown every second.")
try:
    while True:
        print("Position:", pyautogui.position())
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped.")
