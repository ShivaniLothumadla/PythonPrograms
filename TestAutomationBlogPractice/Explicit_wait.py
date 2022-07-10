from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path='c:\Drivers\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='C:\Drivers\geckodriver-v0.30.0-win64\geckodriver.exe')
# driver = webdriver.Edge(executable_path='C:\Drivers\edgedriver_win64\msedgedriver.exe')
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
size = driver.get_window_size()
print('##################', size, '################')
driver.set_window_size(size['width']-500, size['height']-500)
size = driver.get_window_size()
print('##################', size, '################')
wait = WebDriverWait(driver, 10)
wikipedia = wait.until(ec.presence_of_element_located((By.ID, 'Wikipedia1_wikipedia-search-input')))
driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input').send_keys('netherlands')
# driver.close()
