#one value#


#multiple value
def return_without_argument():
    a=13
    b=23
    c=45
    d=23

    return a,b,c,d
x= return_without_argument()
ad=0
for i in x:
    ad=ad+i
    print(i)
print(ad)

