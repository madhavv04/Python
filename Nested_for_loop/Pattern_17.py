for i in range(1,6):
    for j in range(1,6):
        if i==j or i+j==4 or i+j==6 or i+j==8:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()