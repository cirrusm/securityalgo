from selenium import webdriver
import time

option = webdriver.ChromeOptions()
web = webdriver.Chrome(options=option)

web.get('https://www.archives.com/optout')

time.sleep(1)

web.find_element_by_xpath('//*[@id="OptoutFirstName"]').send_keys('hi')