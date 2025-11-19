for i in range(5):
    for j in range(5):
        if j==0 or j==2 or j==4:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

print()

for i in range(5):
    for j in range(5):
        if j%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()