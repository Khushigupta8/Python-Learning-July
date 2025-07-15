def isarea(a, b):
    area = a * b
    print(area)
def iggmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def average(a,b):
        print("the avg of a and b is" , (a+b)/2)
def isslesser(a=2,b=5):
        pass
# def average(a,b,c=1):
#     print("the avg is:", (a+b+c)/2)
# average(3,4)
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        # print("Average is:", sum/len(numbers))
    # average(*numbers)
    # average(2,3,4,8)
    return sum/len(numbers)
c=average(5,6,2)
print(c)
a = 5
b = 3
isarea(a, b)
iggmean(a,b)
c = 10
d = 20
isarea(c, d)
iggmean(c,d)

