i=0
while i<7:
    print(i)
    i=i+1
# for i in range(6):
#     print(i)
    if i==4:
        break
else:
    print("sorry no i")
a=30
b=50
print("A") if a>b else (print("=")) if a==b else print("B")