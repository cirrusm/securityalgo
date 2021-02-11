from bs4 import BeautifulSoup
import requests


r = requests.get('https://www.spokeo.com/Cirrus-Mokhtari/California/Irvine')
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find('div', {'class': 'g'})
print(results)