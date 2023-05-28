name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

dst = dict()

for line in handle :
     if line.startswith("From ") :
            words = line.split()

            # the time part in list of words
            word = words[5] 

            # using slicing, get the hrs part from word
            hrs = word[:2]
            
            # update the count (value) of hrs (key) if not present, default value 0 is returned
            dst[hrs] = dst.get(hrs, 0) + 1

# dynamic list, similar to for loop (or using lst = dst.___()) (loop through values and add them to list)
# (k,v) is used to sort based on hrs (key), as we need need smallest to largest value of hrs with their count           
lst = sorted([(k,v) for (k,v) in dst.items()])

for hours,count in lst:
    print(hours,count)