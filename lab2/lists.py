Example
Create a List:

    thislist = ["apple", "banana", "cherry"]
    print(thislist)


Example
Lists allow duplicate values:

    thislist = ["apple", "banana", "cherry", "apple", "cherry"]
    print(thislist)


Example
Print the number of items in the list:

    thislist = ["apple", "banana", "cherry"]
    print(len(thislist))


Example
String, int and boolean data types:

    list1 = ["apple", "banana", "cherry"]
    list2 = [1, 5, 7, 9, 3]
    list3 = [True, False, False]


Example
A list with strings, integers and boolean values:

    list1 = ["abc", 34, True, 40, "male"]


What is the data type of a list?

    mylist = ["apple", "banana", "cherry"]
    print(type(mylist))


Example
Using the list() constructor to make a List:

    thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
    print(thislist)


Example
Print the second item of the list:

    thislist = ["apple", "banana", "cherry"]
    print(thislist[1])


Print the last item of the list:

    thislist = ["apple", "banana", "cherry"]
    print(thislist[-1])


Example
Return the third, fourth, and fifth item:

    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:5])


Example
This example returns the items from the beginning to, but NOT including, "kiwi":

    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[:4])


Example
This example returns the items from "cherry" to the end:

    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:])


Example
This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[-4:-1])


Example
Check if "apple" is present in the list:

    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


Example
Change the second item:

    thislist = ["apple", "banana", "cherry"]
    thislist[1] = "blackcurrant"
    print(thislist)


Example
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    thislist[1:3] = ["blackcurrant", "watermelon"]
    print(thislist)


Example
Change the second value by replacing it with two new values:

    thislist = ["apple", "banana", "cherry"]
    thislist[1:2] = ["blackcurrant", "watermelon"]
    print(thislist)


Example
Change the second and third value by replacing it with one value:

    thislist = ["apple", "banana", "cherry"]
    thislist[1:3] = ["watermelon"]
    print(thislist)


Example
Insert "watermelon" as the third item:

    thislist = ["apple", "banana", "cherry"]
    thislist.insert(2, "watermelon")
    print(thislist)


Example
Using the append() method to append an item:

    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)


Example
Insert an item as the second position:

    thislist = ["apple", "banana", "cherry"]
    thislist.insert(1, "orange")
    print(thislist)


Example
Add the elements of tropical to thislist:

    thislist = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]
    thislist.extend(tropical)
    print(thislist)
The elements will be added to the end of the list.


Example
Add elements of a tuple to a list:

    thislist = ["apple", "banana", "cherry"]
    thistuple = ("kiwi", "orange")
    thislist.extend(thistuple)
    print(thislist)


Example
Remove "banana":

    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    print(thislist)


Example
Remove the second item:

    thislist = ["apple", "banana", "cherry"]
    thislist.pop(1)
    print(thislist)


Example
Remove the first item:

    thislist = ["apple", "banana", "cherry"]
    del thislist[0]
    print(thislist)
Delete the entire list:

    thislist = ["apple", "banana", "cherry"]
    del thislist


Example
Clear the list content:

    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist)


ExampleGet your own Python Server
Print all items in the list, one by one:

    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
    print(x)


Example
Print all items by referring to their index number:

    thislist = ["apple", "banana", "cherry"]
    for i in range(len(thislist)):
    print(thislist[i])


Example
Print all items, using a while loop to go through all the index numbers

    thislist = ["apple", "banana", "cherry"]
    i = 0
    while i < len(thislist):
    print(thislist[i])
    i = i + 1


Example
A short hand for loop that will print all items in a list:

    thislist = ["apple", "banana", "cherry"]
    [print(x) for x in thislist]