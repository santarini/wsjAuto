import subprocess
import time
import pyautogui
subprocess.Popen(r"C:\Program Files\Trust.Zone VPN Client\trustzone.exe", close_fds=True)
time.sleep(5)
startButton = pyautogui.locateOnScreen('trustZoneStartButton.png', grayscale=True, confidence=.5)
startButton = pyautogui.center(startButton)
pyautogui.moveTo(startButton)
pyautogui.click(button='left', clicks=1, interval=0.25)
#pyautogui.click(startButton[0],startButton[1])
