import subprocess
import time
import pyautogui
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4 as bs
import datetime


def startVPN():
    pyautogui.moveTo(158, 1700)
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
    time.sleep(3)

def stopVPN():
    gatewayIP = requests.get('https://api.ipify.org/?format=json')
    print(gatewayIP.text)
    stopButton = pyautogui.locateOnScreen('trustZoneEndButton.png', grayscale=True, confidence=.5)
    stopButton = pyautogui.center(stopButton)
    pyautogui.moveTo(stopButton)
    pyautogui.click(button='left', clicks=1, interval=0.25)
    #pyautogui.click(startButton[0],startButton[1])
    time.sleep(5)

def closeVPN():
    closeButton = pyautogui.locateOnScreen('vpnExit.png', grayscale=True, confidence=.5)
    closeButton = pyautogui.center(closeButton)
    pyautogui.moveTo(closeButton)
    pyautogui.click(button='left', clicks=1, interval=0.25)
    time.sleep(2)
    closeOkButton = pyautogui.locateOnScreen('vpnExitOk.png', grayscale=True, confidence=.75)
    closeOkButton = pyautogui.center(closeOkButton)
    pyautogui.moveTo(closeOkButton)
    pyautogui.click(button='left', clicks=1, interval=0.25)
    time.sleep(5)
    gatewayIP = requests.get('https://api.ipify.org/?format=json')
    print(gatewayIP.text)
    #pyautogui.click(startButton[0],startButton[1])

def fetchWSJ():
    d = datetime.datetime.today()
    #print(d.strftime('%B %d, %Y'))
    dateString = d.strftime('%B %#d, %Y')
    dateString = dateString.strip()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    #driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe", chrome_options=chrome_options)
    driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")
    driver.set_window_size(480,200)
    driver.get('https://thepiratebay.org/user/surferbroadband/')
    response = driver.page_source
    #searchTable = driver.find_element_by_id('searchResult')

    soup = bs.BeautifulSoup(response, 'lxml')
    searchTable = soup.find("table", {"id": "searchResult"})
    searchTableBody = searchTable.find('tbody')
    trList = searchTableBody.findAll('tr')

    for tr in trList:
        for td in tr.findAll('td'):
            if dateString in str(td):
                currentTD = str(td)
                magnetLink = "magnet" + currentTD.split('href="magnet')[1].split('"')[0]

    #subprocess.Popen(['runas', '/noprofile', '/user:Administrator', r"C:\Users\santa\Downloads\uTorrent.exe"], close_fds=True)

    driver.get(magnetLink)

    time.sleep(2)

    # click chrome prompt
    chromePrompt = pyautogui.locateOnScreen('chromePrompt.png', grayscale=True, confidence=.5)
    chromePrompt = pyautogui.center(chromePrompt)
    pyautogui.moveTo(chromePrompt)
    pyautogui.click(button='left', clicks=1, interval=0.25)

    time.sleep(10)

####    #bypass admin auth
##    pyautogui.hotkey('left')
##    pyautogui.hotkey('enter')
##    time.sleep(5)

    #paste destination path
    basePathDest = r"C:\Users\santa\OneDrive\WSJ\2019"
    #fileName = d.strftime('%a%b%d')
    #pyautogui.typewrite(basePathDest + '\\' +  fileName + '.pdf\n')
    pyautogui.typewrite(basePathDest + "\n")
##    pyautogui.keyDown('tab')
##    pyautogui.keyDown('tab')
##    pyautogui.typewrite(fileName + ".pdf\n")
    #pyautogui.keyDown('enter')
    #pyautogui.keyUp('enter')
    time.sleep(90)

    #clean up
    #delete download

    torRef = pyautogui.locateOnScreen('finished.png', confidence=.9)
    torRef = pyautogui.center(torRef)
    pyautogui.moveTo(torRef)
    time.sleep(5)
    pyautogui.click(button='right', clicks=1, interval=0.25)

    #delete the torrent
    i = 0
    while i < 15:
        pyautogui.hotkey('down')
        i+=1
    pyautogui.hotkey('right')
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)

    #close utorrent
    pyautogui.hotkey('alt', 'f4')

    #close browser
    driver.quit()

#start the vpn
startVPN()
#start the download
fetchWSJ()
#turn off vpn
stopVPN()
#exit vpn client
closeVPN()
print("Pau.")
