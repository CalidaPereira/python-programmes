def gcd(a,b):
   r = a % b
   while r!=0:
       a = b 
       b = r
       r = a % b 
   return b

print(gcd(8,4))
print(gcd(60,96))