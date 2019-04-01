import subprocess
import time
import pyautogui
subprocess.Popen(r"C:\Program Files\Trust.Zone VPN Client\trustzone.exe", close_fds=True)
time.sleep(5)
startButton = pyautogui.locateOnScreen('trustZoneStartButton.png', grayscale=True, confidence=.5)
print(startButton)
