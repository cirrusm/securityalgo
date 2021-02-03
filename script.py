import webbrowser


## SPOKEO URL

## INPUTS
## URL TO PROFILE THAT NEEDS TO BE DELETED + EMAIL ADRESS TO SEND CONFIRMATION LINK TO
opt_out = 'https://www.spokeo.com/optout'
profile = "Please enter the url to the profile you would like to delete"
email_adress = 'Please Enter Your Email'
## OUTPUTS


def remove_profile(email, url):
    webbrowser.open(opt_out)
## OPEN SPOKEO URL
## TYPE PROFILE URL INTO URL INPUT FIELD
## TYPE EMAIL ADRESS URL INTO EMAIL ADRESS FIELD

## MOVE MOUSE TO "IM NOT A ROBOT CHECKBOX"
## CLICK IM NOT A ROBOT CHECKBOX

## CLICK REMOVE THIS LISTING

remove_profile('hi', 'hi')