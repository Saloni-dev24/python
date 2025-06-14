# fibonacci series
# n=int(input("enter the number"))
# a=0 
# b=1
# i=0
# c=0
# while (i<=10):
#   print(c)
#   a=b
#   b=c
#   c=a+b
#   i=i+1

# n=int(input("enter the no.")) #1+2+3+4.......
# sum = 0
# for i in range(1,n+1):
#     sum += i
#     print("natural no.",sum)


# n=int(input("enter the number"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+(i**2)

#     print(sum)


n=int(input("enter the number"))
sum=0
for i in range(1,n+1):
    if(i%2==0):
        sum=sum+(i**3)
    else:
        sum=sum+(i**2)
    print(sum)                                                          j 