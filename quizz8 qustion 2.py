print(" eutimio machuca parra")
print ("This program recivs a parameter as a list and returns the sum of all numbers,  and show you numbers divisible by 3")
def find_threes(x):
    sum = 0
    for i in (x):
        if(i % 3 == 0):
            sum = sum + i
    return sum
 
x = [ 0,4,2,6,9,8,3,12]
ans= find_threes(x)
print ("The sum of all multiples of 3 in", x , "is:", ans)