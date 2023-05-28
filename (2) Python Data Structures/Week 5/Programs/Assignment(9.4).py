name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"
    
handle = open(name)

dst =  dict()

for line in handle :
     if line.startswith("From ") :
            words = line.split()

            # the email part in list of words
            word = words[1] 
            
            # update the count (value) of word (key) if not present, default value 0 is returned
            dst[word] = dst.get(word, 0) + 1

# dynamic list, similar to for loop (or using lst = dst.___()) (loop through values and add them to list) with REVERSE (thus descending order)
# (v,k) is used to sort based on count (value), as we need need largest value at start           
lst = sorted([(v,k) for (k,v) in dst.items()], reverse=True)

# list in form of value, key
(countMax, emailMax) = lst[0]

print(emailMax,countMax)