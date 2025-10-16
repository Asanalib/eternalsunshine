import re


#1

a=input()
x=re.search ("ab*", a)

print (x)


#2

a=input()
x=re.search ("ab{2}|| b{3}", a)
print (x)


#3

a=input()
x=re.findall ("[a-z]_", a)
print (x)


#4
a=input()
x=re.findall ("[A-Z]{1}[a-z]", a)
print (x)


#5
a=input()
x=re.search ("a.+b$", a)
print (x)


#6
a=input()
x=re.sub ("[ , .]", ";", a)
print (x)


#7
a=input()
b=re.split('_', a)
x=b[0]+''.join (i.capitalize() for i in b[1:])
print (x)


#8
a=input()
x=re.split ("[A-Z]", a)
print (x)


#9
a=input()
x=re.sub(r'([A-Z])', r' \1', a).strip()
print (x)


#10
a=input()

x=re.sub(r'([A-Z])', r"_\1", a)
print (x.lower())