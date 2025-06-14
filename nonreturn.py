# def addition():
#     a=int(input("enter the no.1:"))
#     b=int(input("enter the no.2:"))
#     c=a+b
#     print(c)
# addition()

# def simple():
#     p=int(input("enter the no.1:"))
#     r=int(input("enter the no.2:"))
#     t=int(input("enter the no.3:"))
#     SI=(p*r*t)/100
#     print(SI)
# simple()

a=input("enter a character to check=")
s=a.lower()
if(s=="a" or s=="e" or s=="i" or s=="o" or s=="u"):
    print("this is vowel")
else:
    print(" this is consonet")

n=int(input("enter the no."))   #to find armstong
r=n
a=n%10
n=n//10
b=n%10
n=n//10
s=(n**3)+(b**3)+(a**3)
if r==s:
     print("this no. is armstrong",s)
else:
     print("not armstrong",r)



