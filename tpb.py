import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4 as bs

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe", chrome_options=chrome_options)
#driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")

driver.get('https://thepiratebay.org/user/surferbroadband/')

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
