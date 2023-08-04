

'''

FLASH SALES

'''
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



os.environ['PATH'] += (r"D:\\Documents\\Code\\Python\\Selenium\\chrome-win64")

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.jumia.co.ke/')

CONT = input("Press 1 To Proceed And 2 To End...\n")

if CONT == "2":
    driver.quit()

else:
    driver.get('https://www.jumia.co.ke/flash-sales/')

print("hello world")



time.sleep(1000000)


