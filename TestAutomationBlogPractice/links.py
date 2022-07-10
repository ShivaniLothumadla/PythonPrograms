from selenium import webdriver

driver = webdriver.Chrome(executable_path='c:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://testautomationpractice.blogspot.com/')
links = driver.find_elements_by_tag_name('a')
print('Number of links:', len(links))
for link in range(links):
    if links[link].text:
        print(links[link].text)
        links[link].click()
        windows = driver.window_handles
        driver.switch_to.window(windows[links[link]])
        print(driver.title)
        driver.switch_to.window(windows[0])
