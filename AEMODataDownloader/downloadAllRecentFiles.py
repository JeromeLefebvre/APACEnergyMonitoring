from bs4 import BeautifulSoup
import requests

r = requests.get('http://nemweb.com.au/Reports/CURRENT/Operational_Demand/ACTUAL_HH/')
soup = BeautifulSoup(r.content, "lxml")

for link in soup.findAll('a', href=True):
    print(link['href'])
