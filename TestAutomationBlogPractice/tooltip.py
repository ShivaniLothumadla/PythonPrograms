from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
# tooltip
# driver = webdriver.Edge(executable_path='C:\Drivers\edgedriver_win64\msedgedriver.exe')
driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
tooltip = driver.find_element_by_id('age')
driver.execute_script('arguments[0].scrollIntoView();', tooltip)
actions = ActionChains(driver)
actions.move_to_element(tooltip).click().perform()
# msg = driver.find_element_by_xpath("//*[@title='That's what this widget is']")
# wait = WebDriverWait(driver, 10)
# wait = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, 'age')))
name = tooltip.get_attribute('title')
print(name)
