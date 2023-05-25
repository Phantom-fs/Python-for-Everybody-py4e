hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)

if h > 40 :
    pay = (40 * r) + (1.5 * r * (h - 40))
 
else :
    pay = h * r    
    
print(pay)