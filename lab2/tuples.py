Example
Create a Tuple:

    thistuple = ("apple", "banana", "cherry")
    print(thistuple)


Tuple Items
    Tuple items are ordered, unchangeable, and allow duplicate values.

    Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

    Ordered
    When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

    Unchangeable
    Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


Example
Tuples allow duplicate values:

    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
    print(thistuple)


Example
Print the number of items in the tuple:

    thistuple = ("apple", "banana", "cherry")
    print(len(thistuple))


Example
One item tuple, remember the comma:

    thistuple = ("apple",)
    print(type(thistuple))

    #NOT a tuple
    thistuple = ("apple")
    print(type(thistuple))


Example
String, int and boolean data types:

    tuple1 = ("apple", "banana", "cherry")
    tuple2 = (1, 5, 7, 9, 3)
    tuple3 = (True, False, False)


Example
A tuple with strings, integers and boolean values:

    tuple1 = ("abc", 34, True, 40, "male")


What is the data type of a tuple?

    mytuple = ("apple", "banana", "cherry")
    print(type(mytuple))


Example
Using the tuple() method to make a tuple:

    thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
    print(thistuple)


Python Collections (Arrays)
    There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members