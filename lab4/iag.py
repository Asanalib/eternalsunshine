#1
def square (a):
    for i in range (1, a+1):
        yield i**2


a= int (input())

for i in square (a):
    print (i)


#2
def even (b):
    for i in range (1, b+1):
        if i%2==0:
            yield i
        else:
            pass 

b=int (input())

for i in even(b):
    print (i, end=", ")


#3
def div (c):
    for i in range (0, c+1):
        if i%3==0 and i%4==0:
            yield i;
        else:
            pass


c= int(input())
for i in div (c):
    print (i)


#4
def squares (a, b):
    for i in range (a, b+1):
        yield i**2

a=int(input())
b=int(input())

for i in squares (a, b):
    print (i)


#5
def down (n):
    while n>=0:
        yield n
        n-=1

n=int(input())

for i in down (n):
    print (i)