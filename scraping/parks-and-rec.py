import json
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

base_url = 'http://www.seattle.gov/'

data = []


def parseRoot(url):
    time.sleep(0.1)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for header in soup.find_all("h2", class_="paginationTitle"):
        yield parsePark(header.a.string, header.a['href'])
        
def parsePark(name, url):
    time.sleep(0.1)
    response = requests.get(base_url + url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    c = soup.find_all("div", class_="parkHoursAndContactContainer")
    address_a = c[0].find_all('a')[0]
    address = address_a.contents[-1].string
    map_link = address_a['href']
    
    amenities = [span['title'] for span in soup.select("div.amenities > span.pa")]
    
    return {
        'name': name,
        'url': base_url + url,
        'address': address,
        'map': map_link,
        'amenities': amenities
    }

roots = [
    'http://www.seattle.gov/parks/find/parks/parks-a-d',
    'http://www.seattle.gov/parks/find/parks/parks-e-h',
    'http://www.seattle.gov/parks/find/parks/parks-i-l',
    'http://www.seattle.gov/parks/find/parks/parks-m-p',
    'http://www.seattle.gov/parks/find/parks/parks-q-t',
    'http://www.seattle.gov/parks/find/parks/parks-u-z'
]

data = list([park for root in roots for park in parseRoot(root)])

with open('parks-and-rec.json', 'w') as f:
    json.dump(data, f, indent=2)