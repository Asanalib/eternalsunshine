Example
Print i as long as i is less than 6:

    i = 1
    while i < 6:
    print(i)
    i += 1


With the break statement we can stop the loop even if the while condition is true:

Example
Exit the loop when i is 3:

    i = 1
    while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


Example
Continue to the next iteration if i is 3:

    i = 0
    while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


Example
Print a message once the condition is false:

    i = 1
    while i < 6:
    print(i)
    i += 1
    else:
    print("i is no longer less than 6")

