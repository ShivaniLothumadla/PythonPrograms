from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
print(driver.current_url)
wait = WebDriverWait(driver, 20)
wait.until(ec.presence_of_element_located((By.ID, 'demo-simple-context-menu')))
assert driver.find_element_by_id('demo-simple-context-menu').is_displayed(), "'Demo: Simple Context Menu' is not displayed"
# assert driver.find_element_by_xpath('/html/body/div/section/div/div/div/a').is_displayed(), '" Fork on GitHub" is not displayed'
element = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
driver.execute_script('arguments[0].scrollIntoView();', element)
actions = ActionChains(driver)
actions.context_click(element).perform()