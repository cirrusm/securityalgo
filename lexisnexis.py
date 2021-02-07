from selenium import webdriver
import time

## INPUT VARIABLES
# firstname = 'Cirrus'
# lastname = 'Mokhtari'
# address = '4501 surrey drive'
# city = 'Corona del mar'
# zip_code = '92625'

def lexis(firstname, lastname, address, city, zip_code):
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
    web.find_element_by_xpath('//*[@id="nameFirst"]').send_keys(firstname)
    web.find_element_by_xpath('//*[@id="nameLast"]').send_keys(lastname)
    web.find_element_by_xpath('//*[@id="optout"]/div[4]/label[4]/div/a[3]').click()

    # FILL OUT ADRESS/CITY/ZIP SELECT STATE DROPOWN
    web.find_element_by_xpath('//*[@id="addressLine1"]').send_keys(address)
    web.find_element_by_xpath('//*[@id="addressCity"]').send_keys(city)
    web.find_element_by_xpath('//*[@id="addressState"]/option[7]').click()
    web.find_element_by_xpath('//*[@id="addressZip"]').send_keys(zip_code)
    web.find_element_by_xpath('//*[@id="optout"]/div[5]/div[2]/a[3]').click()

    #CLICK SUBMIT
    web.find_element_by_xpath('//*[@id="optout"]/div[6]/div[2]/a[2]').click()

    print(f'A request has been sent to LexisNexis to remove your data, please check your email for a confirmation link')