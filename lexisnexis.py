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
web.find_element_by_xpath('//*[@id="optout"]/div[4]/label[4]/div/a[3]').click()

# FILL OUT ADRESS/CITY/ZIP SELECT STATE DROPOWN
web.find_element_by_xpath('//*[@id="addressLine1"]').send_keys('4501 Surrey Drive')
web.find_element_by_xpath('//*[@id="addressCity"]').send_keys('Corona Del Mar')
web.find_element_by_xpath('//*[@id="addressState"]/option[7]').click()
web.find_element_by_xpath('//*[@id="addressZip"]').send_keys('92625')
web.find_element_by_xpath('//*[@id="optout"]/div[5]/div[2]/a[3]').click()

#CLICK SUBMIT
web.find_element_by_xpath('//*[@id="optout"]/div[6]/div[2]/a[2]').click()