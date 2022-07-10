from selenium import webdriver


driver = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.expedia.com/')
driver.maximize_window()
print(driver.title)
logo = driver.find_element_by_css_selector('.uitk-header-brand-logo')
logo.is_displayed()
# print(text.text)
tabs = driver.find_element_by_css_selector('.uitk-tabs.uitk-tabs-natural.background-primary.uitk-tabs-default.uitk-tabs-with-border.uitk-tabs-natural-center-align.uitk-spacing.lobNavigationFormWithTabs.formAlignedTabs.uitk-spacing-margin-blockstart-three')
print(tabs)
# tab = driver.find_element_by_css_selector(f'{tabs}>li:nth-type-of(4)')
# print(tab.text)