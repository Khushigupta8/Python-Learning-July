import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))
print(timestamp)
timestamp=int(time.strftime('%M'))
print(timestamp)
timestamp=int(time.strftime('%S'))
print(timestamp)
if(timestamp<12):
    print("Good Morning Sir")
elif(timestamp==12):
    print("Good AFternoon sir")
else:
    print("Good evening sir")