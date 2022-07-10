from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
source = driver.find_element_by_xpath('//*[@id="draggable"]/p')
driver.execute_script('arguments[0].scrollIntoView();', source)
destination = driver.find_element_by_xpath('//*[@id="droppable"]')
actions = ActionChains(driver)
# actions.drag_and_drop(source, destination).perform()
# actions.click_and_hold(source).release(destination).perform()
# source_e = driver.find_element_by_xpath('//*[@id="gallery"]/li[1]/img')
# destination_e = driver.find_element_by_xpath('//*[@id="trash"]')
# driver.execute_script('arguments[0].scrollIntoView();', source_e)
# actions.click_and_hold(source_e).perform()
# actions.send_keys(Keys.PAGE_DOWN).perform()
# actions.send_keys(Keys.PAGE_UP).perform()
# actions.release(destination_e).perform()

# resizable
# arrow =driver.find_element_by_xpath('//*[@id="resizable"]/div[3]')
# driver.execute_script('arguments[0].scrollIntoView();', arrow)
# actions.move_to_element(arrow).perform()
# actions.click_and_hold(arrow).perform()

