from selenium import webdriver

driver = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get("http://www.amazon.com/")
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

#Adding a cookie
cookie = {'name': 'shivani', 'value': '1234'}
new_cookie = driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
# deleting cookie
delcookie = driver.delete_cookie('shivani')
print(delcookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
deleteall = driver.delete_all_cookies()
print(deleteall)




