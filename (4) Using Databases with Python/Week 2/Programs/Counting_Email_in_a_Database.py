import sqlite3
import re

conn = sqlite3.connect('emailORG.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fhand = input('Enter file name: ')

try :
    fdata = open(fhand)
    
except :
    print('File cannot be opened:', fhand)
    quit()
    
orgs = dict()

for line in fdata :
    if not line.startswith('From: ') : continue
    
    org = re.findall('@([^ ]*)', line)
    org = str(org[0])
    
    if len(org) == 0 : continue
    
    orgs[org] = orgs.get(org, 0) + 1
    
for org, count in orgs.items() :
    cur.execute('INSERT INTO Counts (org, count) VALUES (?, ?)', (org, count))

conn.commit()

str_sql = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(str_sql) :
    print(str(row[0]), row[1])
    
cur.close()    
    
# different pattern, but same result, way 2
# Link : https://www.py4e.com/code3/emaildb.py?PHPSESSID=97aa6870ad1f22dd099782c02db24656

#   cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
#   row = cur.fetchone()
#   if row is None :
#       cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
#   else :
#       cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))   