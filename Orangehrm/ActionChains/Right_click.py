from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()
ele = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
action = ActionChains(driver)
action.context_click(ele).perform()