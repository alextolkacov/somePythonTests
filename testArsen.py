import requests

requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup

html = requests.get('https://finance.yahoo.com/').text
soup = BeautifulSoup(html, 'html.parser')
table = soup.find("table")
for line in table:
    l = line.findAll("tr")
    print(l)
