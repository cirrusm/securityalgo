from bs4 import BeautifulSoup
import requests


r = requests.get('https://www.spokeo.com/')
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find('div', id = 'name-header')
print(soup)

#This didnt work