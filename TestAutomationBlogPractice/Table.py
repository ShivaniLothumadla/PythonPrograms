from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.techlistic.com/p/demo-selenium-practice.html')
driver.maximize_window()

#scroll to web element
element = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[1]/th[1]')
driver.execute_script("arguments[0].scrollIntoView();", element)
rows = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr'))
columns = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr[1]/th'))
print("Company"+"                       "+"Contact"+"                       "+"Country")

for r in range(2, rows+1):
    for c in range(1, columns+1):
        value = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr['+str(r)+']/td['+str(c)+']').text
        print(value, end='                  ')
    print()
driver.close()