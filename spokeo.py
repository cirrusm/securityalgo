from selenium import webdriver
import time

profile_url = "THIS IS WHERE THE URL GOES"

## OPEN UP THE WEBPAGE
web = webdriver.Chrome()
web.get('https://www.spokeo.com/optout')

time.sleep(3)
## URL AND INPUT FIELDS
url_field = web.find_element_by_xpath('//*[@id="full_panel"]/div/div/div[1]/div[2]/div/form/div[1]/input')
email_field = web.find_element_by_xpath('//*[@id="full_panel"]/div/div/div[1]/div[2]/div/form/div[2]/input')

url_field.send_keys(profile_url)
time.sleep(4)
email_field.send_keys(email)