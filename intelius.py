from selenium import webdriver
import time
## OPEN INTELIUS PAGE

web = webdriver.Chrome()
web.get('https://www.intelius.com/opt-out/')
## CLICK NO
time.sleep(1)
no_button = web.find_element_by_xpath('//*[@id="button-container"]/a[2]')
no_button.click()
## FILL OUT FIRST NAME LAST NAME STATE EMAIL ADRESS CLICK CONTINUE
time.sleep(1)
first_name_field = web.find_element_by_xpath('//*[@id="first-name"]/div/input')
last_name_field = web.find_element_by_xpath('//*[@id="last-name"]/div/input')
email_field = web.find_element_by_xpath('//*[@id="email"]/div/input')

first_name_field.send_keys('Cirrus')
last_name_field.send_keys('Mokhtari')
email_field.send_keys('Cirrus1994@gmail.com')
time.sleep(1)

web.find_element_by_xpath("//select[@name='state']/option[text()='California']").click()

time.sleep(1)
web.find_element_by_xpath('//*[@id="submit"]/div/button').click()
## CLICK FIRST REMOVE RECORD
time.sleep(1)