import math
# math.factorial(2,3)
result=math.sqrt(9)
print(result)
res=math.factorial(4)
print(res)
#if we want to import any one or particular function from math, then:
from math import sqrt,pi #then math. is not needed
a=sqrt(81)*pi
print(a)
# if want to import all functions at once , then
from math import *#not used or recommended much
#as keyword, for shorthand abbreviation
from math import sqrt as s
b=s(4)
print(s)
#dir- to define all functions
# import math
# print(dir(math))
# import pandas 
# print(dir(pandas))
# from deffunc import welcome,khushi
# welcome()
# print(khushi)
from deffunc import *
welcome()
print(khushi)