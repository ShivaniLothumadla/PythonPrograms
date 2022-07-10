from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
# switching frame
# driver.switch_to.frame('frame-one1434677811')
# element = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-9"]')
# driver.execute_script('arguments[0].scrollIntoView();', element)
# drp = Select(element)
# drp.select_by_visible_text('Evening')
# drp.select_by_value('Radio-0')
# drp.select_by_index(2)

#scroll upto specified pixel
driver.execute_script("window.scrollBy(0,250)", "")
print("scrolled upto 250 pixel")

# scroll to up
driver.execute_script("window.scrollBy(0,-300)", "")
print("scrolled upto 250 pixel")

# scroll to down
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
print("scrolled down completely.")

# driver.close()
