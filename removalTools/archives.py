from selenium import webdriver
import time

option = webdriver.ChromeOptions()
web = webdriver.Chrome(options=option)

web.get('https://www.archives.com/optout')

time.sleep(1)

## Fill out first last adress city state zip and email
web.find_element_by_xpath('//*[@id="OptoutFirstName"]').send_keys('hi')
web.find_element_by_xpath('//*[@id="OptoutLastName"]').send_keys('hiiiiiiiii')
web.find_element_by_xpath('//*[@id="OptoutAddress"]').send_keys('address')
web.find_element_by_xpath('//*[@id="OptoutCity"]').send_keys('city')
web.find_element_by_xpath('//*[@id="OptoutPostalCode"]').send_keys('92625')
web.find_element_by_xpath('//*[@id="OptoutPhoneNumber"]').send_keys('949-878-7186')
web.find_element_by_xpath('//*[@id="OptoutEmail"]').send_keys('cirrus1994@gmail.com')
## click "i am this person"
web.find_element_by_xpath('//*[@id="CopyValues"]').click()
## confirm email?

## additional info
web.find_element_by_xpath('//*[@id="Reason"]').send_keys('I dont want my information available on this site. ')
## click i agree to opt out


#submit the form
web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div/form/div[2]/div[18]/div/input').click()