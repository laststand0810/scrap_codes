flag = False
for x in range(max(2, 4, 1, 6) + 1).__reversed__():
    for y in [2, 4, 1, 6]:
        if x < y:
            print("*", end="")
            flag = True
        else:
            if flag is True:
                print(" ", end="")
    print()
    flag = False
