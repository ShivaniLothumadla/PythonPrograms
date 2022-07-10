from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
driver.find_element(By.CLASS_NAME, 'button').click()
driver.implicitly_wait(2)
admin = driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
user_management = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
users = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')
action = ActionChains(driver)
action.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()
