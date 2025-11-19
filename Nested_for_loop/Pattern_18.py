for i in range(5):
    for j in range(1,5):
        if j == 1 or j == 4:
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()