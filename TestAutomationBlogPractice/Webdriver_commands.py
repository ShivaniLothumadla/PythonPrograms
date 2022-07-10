from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element_by_id("Wikipedia1_wikipedia-search-input").send_keys('New York City')
driver.find_element_by_class_name("wikipedia-search-button").click()
sleep(5)
count = driver.find_elements_by_id("wikipedia-search-result-link")
for i in count:
    i.click()
handles = driver.window_handles

for i in handles:
    driver.switch_to.window(i)
    print('new window title:', driver.title)
    print('new window url:', driver.current_url)
    if driver.title != 'Automation Testing Practice':
        driver.close()
    else:
        handle = driver.current_window_handle

# driver.switch_to.window(handles[driver.current_window_handle])
driver.switch_to.window(handle)
driver.close()