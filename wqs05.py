print(" this program will convert temperature from farenheit to celsius")
f=int(input(" give me your temperature in farenheit"))
c=int(5*(f-32)/9)
print("the temperature in farenheit", f, "your temperature en celsius is", c) 
if( c>=100):
 print("water boils")
else:
 print(" water does not boils")