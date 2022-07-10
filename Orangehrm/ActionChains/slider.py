from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
ele = driver.find_element_by_xpath('//*[@id="slider"]/span')
driver.execute_script('arguments[0].scrollIntoView();', ele)
actions = ActionChains(driver)
actions.move_to_element(ele).click_and_hold(ele)
# actions.click_and_hold(ele)
actions.send_keys(Keys.PAGE_UP).release(ele).perform()
# actions.release(ele).perform()



