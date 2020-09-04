hrs = input("Enter Hours:")
h = float(hrs)

rate = float(input("Enter rate:"))
            
if 0<h<=40:
    pay = h * rate 
else: 
    habove40 = h - 40
    pay = (h*rate)+(habove40*rate*1.5)
    
print(pay)
            