# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1

        # get the part of number and space after (using 'find' method) ':' and 'strip' it (remove whitespaces)
        # then using float method, we get the number in float
        num = float(line[line.find(':')+1 : ].strip())

        total += num
    
print("Average spam confidence:", total/count)
