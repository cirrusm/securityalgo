import addressSearch
import lexisnexis
import archives

## ADD AS MANY WITH NO VERFICIATION REQUIRED AS YOU CAN
## WHEN TESTING, YOU MAY WANT TO REMOVE WEBDRIVER.CHROME() FROM EACH INDIVIDUAL FUNCTION

## INFO SITES MAY NEED:
## GRAB THEM THROUGH INPUT

first_name = 'Cirrus'
last_name = "Mokhtari"
address = "4501 surrey drive"
city = "corona del mar"
state = 'California'
zip_code = '92625'
email = 'cirrus1994@gmail.com'
phone = '949-878-7186'


## PROFILE LINKS  <<<<< MIGHT NOT NEED

## TRY FOR AT LEAST 52cffghffff

addressSearch.address_Search(first_name, last_name, address, city, zip_code, email, state)
lexisnexis.lexis(first_name, last_name, address, state, zip_code)
archives.archives(first_name, last_name, address, city, zip_code, phone, email)