from selenium import webdriver
import time

#kgggg

option = webdriver.ChromeOptions()
firstname = input('Please enter your first name: ')
lastname = input('Please enter your last name: ')
email = input('Please enter your email: ')
state = input('What state are you currently living in?: ')
option.add_argument('--disable-blink-features=AutomationControlled')
## OPEN INTELIUS PAGE

web = webdriver.Chrome(options=option)
web.get('https://www.intelius.com/opt-out/')
## CLICK NO
time.sleep(1)
no_button = web.find_element_by_xpath('//*[@id="button-container"]/a[2]')
no_button.click()
# FILL OUT FIRST NAME LAST NAME STATE EMAIL ADRESS CLICK CONTINUES
time.sleep(1)
first_name_field = web.find_element_by_xpath('//*[@id="first-name"]/div/input')
last_name_field = web.find_element_by_xpath('//*[@id="last-name"]/div/input')
email_field = web.find_element_by_xpath('//*[@id="email"]/div/input')

first_name_field.send_keys(firstname)
last_name_field.send_keys(lastname)
email_field.send_keys(email)
time.sleep(1)

web.find_element_by_xpath(f"//select[@name='state']/option[text()='{state}']").click()

web.find_element_by_xpath('//*[@id="submit"]/div/button').click()
# CLICK FIRST REMOVE RECORD

web.find_element_by_xpath('//*[@id="open-result-1"]').click()

