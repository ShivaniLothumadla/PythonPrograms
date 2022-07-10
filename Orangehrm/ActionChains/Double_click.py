from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver import ActionChains

# driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
# Double click
driver.find_element_by_id('field1').is_displayed()
driver.find_element_by_id('field2').is_displayed()
driver.find_element_by_id('field2').send_keys('shivani')
driver.find_element_by_id('field2').clear()
element = driver.find_element_by_xpath('//*[text()="Copy Text"]')
action = ActionChains(driver)
action.double_click(element).perform()