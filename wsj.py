import subprocess
import time
import pyautogui
import requests

def startVPN():
    gatewayIP = requests.get('https://api.ipify.org/?format=json')
    print(gatewayIP.text)
    subprocess.Popen(r"C:\Program Files\Trust.Zone VPN Client\trustzone.exe", close_fds=True)
    time.sleep(10)
    startButton = pyautogui.locateOnScreen('trustZoneStartButton.png', grayscale=True, confidence=.5)
    startButton = pyautogui.center(startButton)
    pyautogui.moveTo(startButton)
    pyautogui.click(button='left', clicks=1, interval=0.25)
    #pyautogui.click(startButton[0],startButton[1])
    time.sleep(15)
    gatewayIP = requests.get('https://api.ipify.org/?format=json')
    print(gatewayIP.text)
#https://thepiratebay.org/user/surferbroadband/

startVPN()
