print(" Eutimio MAchuca Parra A01630244 ")
def factorial(n):
    x=1
    y=1
    while(x<n):
        x=x+1
        y=y*x
    return y

again=1
while(again==1):
    num=int(input("give me a number"))
    if(num<0):
        print(num, " isn't factorial number")
        
    else:
        ans = factorial(num)
        print(" factorial of ", num, "is", ans)
    again=int(input("do you want entry other number? 1-no 0-no: "))
    if(again!=1 and again!=2):
         print(" invalid option")
         again= int(input(" try again, 1-yes 2-no: "))
    