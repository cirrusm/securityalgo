import addressSearch
import lexisnexis

## ADD AS MANY WITH NO VERFICIATION REQUIRED AS YOU CAN
## WHEN TESTING, YOU MAY WANT TO REMOVE WEBDRIVER.CHROME() FROM EACH INDIVIDUAL FUNCTION

## INFO SITES MAY NEED:
## GRAB THEM THROUGH INPUT

first_name = 'Cirrus'
last_name = "Mokhtari"
address = "4501 surrey drive"
city = "corona del mar"
state = 'california'
## ZIP
## EMAIL
## PHONE

## PROFILE LINKS  <<<<< MIGHT NOT NEED

## TRY FOR AT LEAST 5

addressSearch.address_Search('Cirrus', 'Mokhtari', '4501 surrey drive', 'corona del mar', '92625', 'cirrus1994@gmail.com', 'California')
lexisnexis.lexis('Cirrus', 'Mokhtari', '4501 surrey drive', 'California', '92625')