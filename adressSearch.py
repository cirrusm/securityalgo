from selenium import webdriver
import time

## INPUT VARIABLES
firstname = 'Cirrus'
lastname = 'Mokhtari'
address = '4501 surrey drive'
city = 'Corona del mar'
zip_code = '92625'
email = 'Cirrus1994@gmail.com'

web = webdriver.Chrome()
web.get('https://www.addresssearch.com/remove-info.php')

web.find_element_by_xpath('//*[@id="body_container"]/div[1]/div/form/table/tbody/tr[1]/td[2]/input[1]').send_keys(firstname)