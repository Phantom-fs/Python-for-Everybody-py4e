import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/known_by_Sinead.html"

for i in range(7):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    tags = soup('a')
    
    url = tags[17].get('href', None)
    
text = re.findall('by_(.+).html', url)

print(text)