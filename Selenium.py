import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += (r"D:\\Documents\\Code\\Python\\Selenium\\chrome-win64")

driver = webdriver.Chrome()

driver.get('https://www.jumia.co.ke/')



my_choice = input("Which Category Do You Want Us To Explore Today??\n1)Supermarket\n2)Health & Beauty\n3)Appliances\n4)Phones & Tablets\n5)Computing\n6)TVs & Audio\n7)Fashion\n8)Gaming\n9)Baby Products\n10)Sporting Goods\n11)Others\n\n\nWhat's Your Choice??\n")

if my_choice == "1":
    my_element = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.jumia.co.ke/groceries/"]')

    my_element.click()


time.sleep(105)
