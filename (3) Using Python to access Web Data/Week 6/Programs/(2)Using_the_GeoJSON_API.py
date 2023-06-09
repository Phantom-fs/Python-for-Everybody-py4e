import urllib.request, urllib.parse, urllib.error
import json

serviceURL = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')
    
    if len(address) < 1:
        break

    url = serviceURL + urllib.parse.urlencode({'address': address, 'key': 42})
    
    print('\nRetrieving', url, '...\n')
    
    data = urllib.request.urlopen(url)
    json_data = data.read().decode()
    
    print('Retrieved', len(json_data), 'characters\n')

    try:
        info = json.loads(json_data)
    except:
        info = None

    if not info or 'status' not in info or info['status'] != 'OK':
        print('==== Failure To Retrieve ====\n\n')
        print(json_data)
        continue
    
    # print(json.dumps(info, indent=4))

    print('Place id :', info['results'][0]['place_id'], '\n\n')