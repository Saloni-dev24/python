# x= lambda a,b:a if a>b else b
# print(x(10,20))

# wap to find maximum from 3 input taken form user using lambda function

# x= lambda a,b,c:a if a>b and a>c else (b if b>a and b>c else c)
# print(x(10,20,50))

# remove all the empty string from the list using filter function

# function ,squence

name=["raj","ram","","sanjay","neeraj"]
def mydata(list):
    if list=="":
        return False
    else:
        return True
mylist=filter(mydata,name)
print(list(mylist))  #['filter.py', 'function.py','main.py','test.py']
x=filter(lambda x:False if x== ""else True,name)
print(list(x))#['filter.py', 'function.py','main.py','test.py']



name=[10,20,30,40,50]
def mydata(list):
    if list=="":
        return False
    else:
        return True
mylist=filter(mydata,name)
print(list(mylist))  #['filter.py', 'function.py','main.py','test.py']
x=filter(lambda x:False if x=10 elseTrue,name)
print(list(x))#['filter.py', 'function.py','main.py','test.py']





