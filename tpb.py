import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4 as bs
import datetime

d = datetime.datetime.today()
print(d.strftime('%B %d, %Y'))
dateString = d.strftime('%B %#d, %Y')
dateString = dateString.strip()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

#driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe", chrome_options=chrome_options)
driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")

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

driver.get(magnetLink)



#find the table
#if the link in the table contains today's date
#go to it's url
#click the magnet Get this Torrent
#choose destination path
#click ok
#wait 3 minutes
#delete download
#close utorrent
#close browser
#turn off vpn
#exit vpn client
#test ip
