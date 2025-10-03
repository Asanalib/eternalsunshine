# 1
class a:
    def __init__(self):
        self.str1 = "" 

    def getString(self):
        self.str1 = input()

    def printString(self):
        print(self.str1.upper())


str = a()       
str.getString()       
str.printString()     

# 2
class shape:
    def __init__(self):
        pass

    def area (self):
        return 0;


class square (shape):
    def __init__(self, len):
        self.len=len

    def area(self):
        return (self.len)**2

a=shape()
print (a.area())

b=square(int(input()))
print(b.area())

#3

class rect(shape):
    def __init__(self, len, wid):
        self.length=len
        self.width=wid

    def area (self):
        return (self.length * self.width)
    
c=rect(int(input()), int(input()))
print (c.area())


#4
import math

class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show (self):
        print (self.x, self.y)

    def move (self , x1, y1):
        self.x=x1
        self.y=y1

    def dist (self, lol):
        return math.sqrt ((self.x-lol.x)**2 + (self.y-lol.y)**2)
    
a=point(int(input()), int(input()))
b=point(int(input()), int(input()))

a.show()
b.show()

print (a.dist(b))

a.move(int(input()), int(input()))
a.show()


#5
class account:
    def __init__ (self, owner, balance):
        self.owner=owner
        self.balance=balance
    
    def deposit (self, amount):
        self.balance += amount
        print(amount,self.balance)

    def withdraw (self,amount):
        if amount>self.balance:
            print ("Withdrawals may not exceed the available balance")
        else:
            self.balance -= amount
            print (amount, self.balance)
    
    acc=account(input(), int(input()))
    acc.deposit (int(input()))
    acc.withdraw (int(input()))


#6

def is_prime (n):
    if n<2: 
        return False

    for i in range (2, int (n**0.5)+1):
        if n % i ==0:
            return False 
        return True
    
    a = list(map(int, input().split()))
    filter=list(filter(lambda x: is_prime(x), a))
    print (filter)