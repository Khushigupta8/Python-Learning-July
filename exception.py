a = input("enter your number: ")
print(f"multiplication table of {a} is:")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print("error")
try:
    num=int(input("enter:"))
except ValueError:#IndexError
    print("incorrect value")
finally : ("i m good")
n=int(input("enter"))
if (n<5 or n>2):
    raise ValueError("err")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    