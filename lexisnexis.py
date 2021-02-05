from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://optout.lexisnexis.com/')

# CLICK 1ST NEXT BUTTON
web.find_element_by_xpath('//*[@id="optout"]/div[1]/div/a').click()
# CLICK 2ND NEXT BUTTON
web.find_element_by_xpath('//*[@id="optout"]/div[2]/div/a[2]').click()
# SELECT OPTION ON DROPDOWN, THEN CLICK 3RD NEXT
web.find_element_by_xpath('//*[@id="reason"]/option[2]').click()
web.find_element_by_xpath('//*[@id="optout"]/div[3]/div[2]/a[2]').click()
# FILL OUT FIRST AND LAST NAME, CLICK NEXT
web.find_element_by_xpath('//*[@id="nameFirst"]').send_keys('Cirrus')
web.find_element_by_xpath('//*[@id="nameLast"]').send_keys('Mokhtari')
# FILL OUT ADRESS/CITY/ZIP SELECT STATE DROPOWN
