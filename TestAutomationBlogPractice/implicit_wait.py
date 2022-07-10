from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path='c:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
driver.implicitly_wait(10)
assert 'Testing' in driver.title, "Page not loaded"

#text fields
driver.switch_to.frame('frame-one1434677811')
driver.find_element_by_name('RESULT_TextField-1').send_keys('Shivani')
driver.find_element_by_id('RESULT_TextField-2').send_keys('Lothumadla')
driver.find_element_by_id("RESULT_TextField-3").send_keys('99999999999')
driver.find_element_by_name('RESULT_TextField-4').send_keys('india')
driver.find_element_by_id('RESULT_TextField-5').send_keys('Siddipet')
driver.find_element_by_id('RESULT_TextField-6').send_keys('sl@gmail.com')

# radio buttons
print(len(driver.find_elements_by_id('RESULT_RadioButton-7_0')))
b_status1 = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').click()
a_status1 = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
b_status2 = driver.find_element_by_id('RESULT_RadioButton-7_1').is_selected()
driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[2]/td/label').click()
a_status2 = driver.find_element_by_id('RESULT_RadioButton-7_1').is_selected()


# #checkboxes
driver.find_element_by_xpath("//*[text()='Sunday']").click()
driver.find_element_by_xpath("//*[text()='Monday']").click()
driver.find_element_by_xpath("//*[text()='Tuesday']").click()
driver.find_element_by_xpath("//*[text()='Wednesday']").click()
driver.find_element_by_xpath("//*[text()='Thursday']").click()
driver.find_element_by_xpath("//*[text()='Friday']").click()

#dropdown
element = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-9"]')
driver.execute_script('arguments[0].scrollIntoView();', element)

options = list(driver.find_elements(By.XPATH, '//*[@id="RESULT_RadioButton-9"]/option'))
for i in range(len(options)):
    if options[i].text == 'Evening':
        options[i].click()
        break
drp = Select(element)
drp.select_by_index(1)
drp.select_by_value('Radio-1')
# drp.select_by_visible_text('Evening')

# search
driver.switch_to.default_content()
driver.find_element_by_id("Wikipedia1_wikipedia-search-input").send_keys('New York City')
driver.find_element_by_class_name("wikipedia-search-button").click()
sleep(5)

#switching to the frame
driver.switch_to.frame('frame-one1434677811')
driver.find_element_by_link_text('Software Testing Tutorials').is_displayed()
driver.find_element_by_partial_link_text('Testing Tuto').is_enabled()
driver.find_element_by_xpath('//*[text()="Software Testing Tutorials"]').is_selected()

# Alert
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[text()="Click Me"]').click()
sleep(2)
driver.switch_to.alert.accept()
print('Accepted')
driver.find_element_by_xpath('//*[text()="Click Me"]').click()
sleep(2)
driver.switch_to.alert.dismiss()
print("Dismissed")

# table
ele = driver.find_element_by_xpath('//*[@id="HTML1"]/div[1]')
driver.execute_script('arguments[0].scrollIntoView();', ele)
rows = len(driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr'))
columns = len(driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th'))
print("BookName"+"                      "+"Author"+"                    "+"Subject"+"                   "+"Price")

for r in range(2, rows+1):
    for c in range(1, columns+1):
        value = driver.find_element_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr['+str(r)+']/td['+str(c)+']').text
        print(value, end='                          ')
    print()



# Double click
driver.find_element_by_id('field1').is_displayed()
driver.find_element_by_id('field2').is_displayed()
driver.find_element_by_id('field2').send_keys('shivani')
driver.find_element_by_id('field2').clear()
element = driver.find_element_by_xpath('//*[text()="Copy Text"]')
action = ActionChains(driver)
action.double_click(element).perform()

