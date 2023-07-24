i = 1
count = 4
while i < 8:
    print(" " * count, end="")
    j = i
    while j > 0:

        print("*", end="")
        j -= 1
    count = count - 1
    i += 2
    print("")