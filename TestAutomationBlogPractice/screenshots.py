from selenium import webdriver

driver = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get("http://testautomationpractice.blogspot.com/")
driver.save_screenshot('C:\screenshots\homepage.png')