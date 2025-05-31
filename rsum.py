n= int (input ("enter the number"))#5
rsum= 0
while (n>0):
    r=n %10
    rev=rsum+r
    n= n//10
    print(rsum)
