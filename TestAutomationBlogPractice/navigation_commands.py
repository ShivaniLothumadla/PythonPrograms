from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.google.com/')
sleep(3)
print(driver.title)

driver.get('http://www.gmail.com/')
sleep(3)
print(driver.title)
# driver.navigate_to('http://www.gmail.com/')

driver.back()
sleep(3)
print(driver.title)
driver.forward()
sleep(3)
print(driver.title)