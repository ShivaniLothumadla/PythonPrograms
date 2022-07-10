'''
get_attribute is a method to get the value of the attribute.
An attribute is like id, name, class and type etc
to use the get_attribute() we have to findout the attribute and then use get_attribute() and pass the name of the attribute of which value you wanted to get.
'''
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.yatra.com/')
sleep(4)
driver.find_element_by_xpath('//*[@class="demo-icon icon-holidays"]').click()
sleep(4)
text = driver.find_element_by_xpath('//*[@class="demo-icon icon-holidays"]').get_attribute('class')
print('@@@@@@@@@@@@@@@@', text, '@@@@@@@@@@@@@@@@')
sleep(5)
driver.quit()
