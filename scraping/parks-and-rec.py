import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def parseRoot(url):
    time.sleep(1)
    response = request.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for header in soup.find_all("h2", class_="paginationTitle"):
        parsePark(header.a.contents, header.a.href);
        
def parsePark(name, link):
    print(name)

roots = [
    'http://www.seattle.gov/parks/find/parks/parks-a-d',
    'http://www.seattle.gov/parks/find/parks/parks-e-h',
    'http://www.seattle.gov/parks/find/parks/parks-i-l',
    'http://www.seattle.gov/parks/find/parks/parks-m-p',
    'http://www.seattle.gov/parks/find/parks/parks-q-t',
    'http://www.seattle.gov/parks/find/parks/parks-u-z'
]    

for root in roots:
    parseRoot(root)
