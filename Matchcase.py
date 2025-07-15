x=int(input("enter a number: "))
match x:
    case 0:
        print(x, " is zero")
    case 1:
        print(x,"is one")
    case _ if x != 2:
        print(x,"x isnot 2")
    case _:
        print("invalid value of x")