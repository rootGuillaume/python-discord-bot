import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.myges.fr/student/planning-calendar')

print(r.status_code)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup)

