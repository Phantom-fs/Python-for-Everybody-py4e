import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter the URL: ')

data = urllib.request.urlopen(url)
json_data = data.read().decode()

info = json.loads(json_data)

count = 0

for item in info['comments']:
    count += item['count']
    
print(count)