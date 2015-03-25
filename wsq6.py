print(" in this program you have to adivinate the number that I'm thinking betweeen a and 100")
import random
y=(random.randint(1,100))
print("shhhh, random is",y)
n=int(0)
x=int(input(" please guess a number between 1 and 100"))
while(x!=y):
   if( x>y):
     print(" its too high")
   else:
      print(" its too low")
   n = n+1
   x = int(input(" please guess a number between 1 and 100"))

print(" you got it")
print(" at the", n, "attempts")
