from selenium import webdriver
import time



def archives(first, last, address, city, zipCode, phone, email):
    option = webdriver.ChromeOptions()
    web = webdriver.Chrome(options=option)
    web.get('https://www.archives.com/optout')

    ## Fill out first last adress city state zip and email
    web.find_element_by_xpath('//*[@id="OptoutFirstName"]').send_keys(first)
    web.find_element_by_xpath('//*[@id="OptoutLastName"]').send_keys(last)
    web.find_element_by_xpath('//*[@id="OptoutAddress"]').send_keys(address)
    web.find_element_by_xpath('//*[@id="OptoutCity"]').send_keys(city)
    web.find_element_by_xpath('//*[@id="OptoutPostalCode"]').send_keys(zipCode)
    web.find_element_by_xpath('//*[@id="OptoutPhoneNumber"]').send_keys(phone)
    web.find_element_by_xpath('//*[@id="OptoutEmail"]').send_keys(email)
    ## click "i am this person"
    web.find_element_by_xpath('//*[@id="CopyValues"]').click()
    ## confirm email?

    ## additional info
    web.find_element_by_xpath('//*[@id="Reason"]').send_keys('I dont want my information available on this site. ')
    ## click i agree to opt out
    web.find_element_by_xpath('//*[@id="AgreeToOptoutPolicy"]').click()


    #submit the form
    web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div/form/div[2]/div[18]/div/input').click()