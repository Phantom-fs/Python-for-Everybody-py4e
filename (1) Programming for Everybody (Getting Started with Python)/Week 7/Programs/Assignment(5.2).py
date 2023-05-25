largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break
    
    else :
        try :
            n = int(num)
            
            if largest is None and smallest is None :
                largest = n
                smallest = n                
            
            if n > largest :
                largest = n
                
            if n < smallest :
                smallest = n
            
        except :
            print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)