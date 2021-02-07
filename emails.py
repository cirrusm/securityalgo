import os
import smtplib

## should prob make this a function 
## pass it an array of objects containing users info, + a profile link for each object
def sendmail(name, url):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('cirrus1994@gmail.com', 'vegasfat1')

        subject = 'Request to remove profile'
        body = """To whom it may concern,
            
            I am an agent removing personal information on behalf of [Full name] and have been unsuccessful from removing data from your website. Per the information provided from your legal privacy policy, please remove the following page from your service: [url]
            """
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('cirrus1994@gmail.com', ['mokhtari@ucsb.edu', 'cirrus1994@gmail.com'], msg)