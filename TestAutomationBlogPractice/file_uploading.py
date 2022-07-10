from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.maximize_window()

driver.get('https://testautomationpractice.blogspot.com/')
driver.switch_to.frame('frame-one1434677811')
element = driver.find_element(By.ID, 'RESULT_FileUpload-10')
driver.execute_script('arguments[0].scrollIntoView();', element)
element.send_keys('C:/Shivani/demofile.txt')
driver.implicitly_wait(2)
driver.close()