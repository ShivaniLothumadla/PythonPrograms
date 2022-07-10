from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
driver.find_element(By.ID, 'datepicker').click()
wait = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.ID, 'ui-datepicker-div')))
def getmonthyear(monthyear):
    return monthyear.split(' ')
def selectdate(exday, exmonth, exyear):
    monthyear = driver.find_element(By.CLASS_NAME, 'ui-datepicker-title').text

    if exyear > getmonthyear(monthyear)[1]:
        while(not (getmonthyear(monthyear)[0] == exmonth and getmonthyear(monthyear)[1] == exyear)):
            driver.find_element(By.XPATH, '//*[text()="Next"]').click()
            monthyear = driver.find_element(By.CLASS_NAME, 'ui-datepicker-title').text
    elif exyear < getmonthyear(monthyear)[1]:
        while (not (getmonthyear(monthyear)[0] == exmonth and getmonthyear(monthyear)[1] == exyear)):
            driver.find_element(By.XPATH, '//*[text()="Prev"]').click()
            monthyear = driver.find_element(By.CLASS_NAME, 'ui-datepicker-title').text

    try:
        driver.find_element(By.XPATH, "//*[text()='"+exday+"']").click()
    except:
        print(f'Selected date: {exday} and month: {exmonth} is not valid')

selectdate("17", "March", "1997")
