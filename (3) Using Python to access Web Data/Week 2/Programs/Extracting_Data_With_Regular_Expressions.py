import re

fileHandle = input('Enter file name: ')

try:
    sum = 0
    
    fhand = open(fileHandle)
    
    for line in fhand :
        line = line.rstrip()
        
        nums = re.findall('[0-9]+', line)
        
        for num in nums :
            sum += int(num)
            
    print(sum)
    
except:
    print('File cannot be opened:', fileHandle)
    exit()