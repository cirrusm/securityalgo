import addressSearch
import lexisnexis

## ADD AS MANY WITH NO VERFICIATION REQUIRED AS YOU CAN
## WHEN TESTING, YOU MAY WANT TO REMOVE WEBDRIVER.CHROME() FROM EACH INDIVIDUAL FUNCTION

## INFO SITES MAY NEED:
## GRAB THEM THROUGH INPUT

## FIRSTNAME
## LASTNAME
## ADDRESS
## CITY
## STATE
## ZIP
## EMAIL
## PHONE

## PROFILE LINKS  <<<<< MIGHT NOT NEED

addressSearch.address_Search('Cirrus', 'Mokhtari', 'address', 'city', 'zip', 'email', 'state')
lexisnexis.lexis('Cirrus', 'Mokhtari', 'address', 'city', 'zip')