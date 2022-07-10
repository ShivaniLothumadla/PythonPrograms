from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.ajio.com/')
driver.maximize_window()
driver.find_element(By.NAME, 'searchVal').click()
driver.find_element(By.XPATH, '//*[text()="shoes"]').click()
# driver.find_element(By.CSS_SELECTOR, '.ReactVirtualized__Grid items')

elements = driver.find_elements(By.CSS_SELECTOR, '.contentHolder')
max_original_price = 0
max_dict = {}
for i in range(6):
    brand = elements[i].find_element(By.XPATH, '//*[@class="contentHolder"]//child::div[@class="brand"]').text
    # brand = driver.find_element(By.CSS_SELECTOR, '.brand').text
    name = elements[i].find_element(By.CSS_SELECTOR, '.nameCls').text
    price = elements[i].find_element(By.CSS_SELECTOR, '.price  ').text
    original_price = elements[i].find_element(By.CSS_SELECTOR, '.orginal-price').text
    discount = driver.find_element(By.CSS_SELECTOR, '.discount').text
    offer_prices = elements[i].find_element(By.CSS_SELECTOR, '.offer-pricess').text
    original_price = int(original_price.split('₹')[1].replace(',', ''))
    if original_price > max_original_price:
        max_original_price = original_price
        max_dict = {
        'max_orignal_price': original_price,
        'max_brand' : brand,
        'max_name' : name,
        'max_price' : price,
        'max_oprice' : original_price,
        'max_discount' : discount,
        'max_offer_price' : offer_prices}
print(max_dict)























# from selenium import webdriver
# from time import sleep
#
#
# driver = webdriver.Chrome(executable_path='C:/web Automation/lcg_uat/venv/Scripts/chromedriver.exe')
# driver.get('https://www.ajio.com/')
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@name="searchVal"]').send_keys('Shoes')
# sleep(2)
# suggestions = driver.find_elements_by_xpath('//*[@id="react-autowhatever-1"]')
# suggestions[1].click()
# products = driver.find_elements_by_xpath('//*[@class="preview"]')
# print(products)
# original_price_list = []
# for product in range(6):
#     info = products[product].text.split('\n')
#     if 'QUICK VIEW' in info:
#         info.remove('QUICK VIEW')
#     Brand = info[0]
#     name = info[1]
#     price = info[2]
#     offer_price = info[3]
#     original_price = info[2].split(' ')[1].split('₹')[1]
#     original_price_list.append(original_price)
# print(original_price_list)
# for i in range(0, len(original_price_list)):
#     if ',' in original_price_list[i]:
#         original_price_list[i] = original_price_list[i].replace(',', '')
#     original_price_list[i] = int(original_price_list[i])
#
# highest_price = max(original_price_list)
# print(highest_price)
# driver.close()


