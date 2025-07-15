print("hello \n i amkhushi")
print(5)
print(18/3)
print(8*3,2+3)
#yess comment
#cntrl+fwd slash to uncomment/vice versa"""
"""
hi"""
# print('my name is kkhushi')
# print("hey", 7 , 6 , sep="-",end="02")
a=10
print(a)
print("the type of a is", type(a))
list1=[9,19,["apple"]]
print(list1)
tuple1=(20,40,'kg')
print(tuple1)
#tuple is immutable list is mutabl;e
dict1={"name":"khushi","age":21}
print(dict1)
print(5**3)
## CALCULATOR IN MAKING
a=20
b=10
print("the value of", a , "+" , b ,"is", a+b)
print("the value of", a , "*" , b ,"is", a*b)
print("the value of", a , "/" , b ,"is", a/b)
print("the value of", a , "-" , b, "is", a-b)
print("the value of", a , "%" , b, "is", a%b)
##TYPECASTING IN PYTHON
A="1"
B="2"
print(int(A)+int(B))
print(A+B)
c=4.2
d=2
print(c+d)
# TAKIG INPUT FROM USER
# e = input()
# print("My name is",e)
# f=input("enter your age")
# print("her age is", f)
# x=input("enter first number: ")
# y=input("enter second number: ")
# print(x+y)
# print(int(x)+int(y))
this="""ji she says she's from the island"""
print(this)
print(this[1])
print("lets use a for loop")
for characters in this:
    print(characters)
    ##STRING SLICING
    names="Vakul,Khushi"
    #doesnt include last index but does first
    print(names[0:5])
    print(len(names))
    print(names[0:-5])
    # print(names[0:len(names)-4])
    nm="harry"
    print(nm[-4:-2])
    #Strings ARE IMMUTABLE
    q="ku sh!!"
    print(q.lower())
    print(q.upper())
    print(q.capitalize())
    print(q.rstrip("!"))
    print(q.replace("ku sh","khushi"))
    print(q.split(" "))
    print(q.center(50))
    print(len(q))
    print(q.endswith("."))
    print(q.endswith("!"))
    print(q.endswith("h!",3,6))
    print(q.find("sh!!"))
    print(q.isalnum())
#CONDITIONAL OPERATORS 
    age=int(input("Enter you age: "))
    print("your age is:",age)
    print(age>18)
    print(age<18)
    print(age==18)
    print(age!=18)
    if (age>18):
        print("you can drive")
    else:
        print("you cannot drive")