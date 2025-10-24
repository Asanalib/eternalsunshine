import math
import re
import time

#1
a=list(map(int, input().split()))

print(math.prod(a))

#2
a=input()
upper=len(re.findall("[A-Z]", a))
lower=len(re.findall("[a-z]", a))
print (upper, lower)

#3

a=input()
b=len(a)

if a==a[::-1]:
    print ("yes")
else:
    print ("no")

#4
a=int(input())
time.sleep((int(input())/1000))
res=pow(a, 0.5)
print(res)

#5
a=eval(input())
c=all(a)
print (c)

