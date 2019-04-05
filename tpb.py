import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4 as bs
import datetime
import pyautogui
import time

##d = datetime.datetime.today()
##print(d.strftime('%B %d, %Y'))
##dateString = d.strftime('%B %#d, %Y')
##dateString = dateString.strip()
##
##chrome_options = webdriver.ChromeOptions()
##chrome_options.add_argument("--incognito")
##
###driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe", chrome_options=chrome_options)
##driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")
##
##driver.get('https://thepiratebay.org/user/surferbroadband/')
##response = driver.page_source
###searchTable = driver.find_element_by_id('searchResult')
##
##soup = bs.BeautifulSoup(response, 'lxml')
##searchTable = soup.find("table", {"id": "searchResult"})
##searchTableBody = searchTable.find('tbody')
##trList = searchTableBody.findAll('tr')
##
##for tr in trList:
##    for td in tr.findAll('td'):
##        if dateString in str(td):
##            currentTD = str(td)
##            magnetLink = "magnet" + currentTD.split('href="magnet')[1].split('"')[0]
##
##driver.get(magnetLink)
##
##time.sleep(3)
##
### click chrome prompt
##chromePrompt = pyautogui.locateOnScreen('chromePrompt.png', grayscale=True, confidence=.5)
##chromePrompt = pyautogui.center(chromePrompt)
##pyautogui.moveTo(chromePrompt)
##pyautogui.click(button='left', clicks=1, interval=0.25)
##
##time.sleep(5)
##
###paste destination path
##basePathDest = r"C:\Users\santa\OneDrive\WSJ\2019"
##fileName = d.strftime('%a%b%d')
##pyautogui.typewrite(basePathDest + '\\' +  fileName + '\n')
###pyautogui.keyDown('enter')
###pyautogui.keyUp('enter')
##time.sleep(60)

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
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)

#close utorrent
pyautogui.hotkey('alt', 'f4')

#close browser
driver.quit()
#turn off vpn
#exit vpn client
#test ip
