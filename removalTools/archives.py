from selenium import webdriver
import time

option = webdriver.ChromeOptions()
web = webdriver.Chrome(options=option)

web.get('https://www.archives.com/optout')

time.sleep(1)

## Fill out first last adress city state zip and email
web.find_element_by_xpath('//*[@id="OptoutFirstName"]').send_keys('hi')
web.find_element_by_xpath('//*[@id="OptoutMiddleName"]').send_keys('hiiiiiiiii')


## click "i am this person"
## confirm email?
## additional info
## click i agree to opt out

web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div/form/div[2]/div[18]/div/input').click()