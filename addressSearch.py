from selenium import webdriver
import time

## INPUT VARIABLES
# firstname = 'Cirrus'
# lastname = 'Mokhtari'
# address = '4501 surrey drive'
# city = 'Corona del mar'
# zip_code = '92625'
# email = 'Cirrus1994@gmail.com'
# state = "California"

## NEED TO UPDATE SELECT

def address_Search(firstname, lastname, address, city, zip_code, email, state):
    web = webdriver.Chrome()
    web.get('https://www.addresssearch.com/remove-info.php')

    # First last name
    web.find_element_by_xpath('//*[@id="body_container"]/div[1]/div/form/table/tbody/tr[1]/td[2]/input[1]').send_keys(firstname)
    web.find_element_by_xpath('//*[@id="body_container"]/div[1]/div/form/table/tbody/tr[1]/td[2]/input[2]').send_keys(lastname)

    # Email

    web.find_element_by_xpath('//*[@id="body_container"]/div[1]/div/form/table/tbody/tr[2]/td[2]/input').send_keys(email)

    #Adress

    web.find_element_by_xpath('//*[@id="address1"]').send_keys(address)
    web.find_element_by_xpath('//*[@id="city"]').send_keys(city)
    web.find_element_by_xpath('//*[@id="body_container"]/div[1]/div/form/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[3]/input').send_keys(zip_code)

    #SELECT STATE

    web.find_element_by_xpath(f"//select[@name='state']/option[text()='{state}']").click()

    # SUBMIT
    web.find_element_by_xpath('//*[@id="body_container"]/div[1]/div/form/table/tbody/tr[4]/td[2]/input').click()

