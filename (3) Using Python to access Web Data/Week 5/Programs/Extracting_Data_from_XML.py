import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
html = urllib.request.urlopen(url).read()

xml_data = html.decode().strip()

tree = ET.fromstring(xml_data)
counts = tree.findall('.//count')

total_count = 0

for count in counts:
    total_count += int(count.text) # type: ignore

print("Total count:", total_count)