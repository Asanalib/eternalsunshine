import os

#1
path=input()
all=os.listdir(path)
print(all)


for i in all:
    full=os.path.join(path, i)
    if os.path.isdir(full):
        print(i, "dir")
    else:
        print(i, "file")

#2
path=input()
if os.access(path, os.F_OK)==True:
    print("exists")
else:
    print("non-existant")

if os.access(path, os.R_OK)==True:
    print("readable")
else:
    print("non-readable")

if os.access(path, os.W_OK)==True:
    print("writable")
else:
    print("non-wtitable")

if os.access(path, os.X_OK)==True:
    print("executable")
else:
    print("non-executable")

#3
path=input()
all=os.listdir(path)


if os.access(path, os.F_OK):
    for i in all:
        full=os.path.join(path, i)
        if os.path.isdir(full):
            print(i, "dir")
        else:
            print(i, "file")
else:
    ("non-existant")

#4
with open("lol.txt", 'r') as f:
    c=f.readlines()

print (len(c))

#5
a=input()

with open("lol.txt", "a") as f:
    f.write(a)

with open ("lol.txt") as f:
    print (f.read())


#6
import string
for i in string.ascii_uppercase:
    file_name=f"{i}.txt"
    with open(file_name, 'w') as file:
        file.write(file_name)
    print (file_name)

#7
src = input()
dest = input()

with open(src, 'r'):
    with open(dest, 'w') :
        dest.write(src.read())

#8

path=input()
if os.access(path, os.F_OK)==True:
    print("exists")
    os.remove(path)
else:
    print("non-existant")