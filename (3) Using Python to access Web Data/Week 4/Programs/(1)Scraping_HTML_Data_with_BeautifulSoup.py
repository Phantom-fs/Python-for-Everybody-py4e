import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_1816616.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')

sum = 0

for tag in tags:
    sum += int(tag.contents[0])
    
print(sum)