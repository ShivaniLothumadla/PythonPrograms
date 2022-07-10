from selenium import webdriver
from time import sleep


driver = webdriver.Chrome(executable_path='C:/web Automation/lcg_uat/venv/Scripts/chromedriver.exe')
driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
sleep(5)
driver.switch_to.alert.accept()
driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
sleep(5)
driver.switch_to.alert.dismiss()
sleep(5)
driver.close()
