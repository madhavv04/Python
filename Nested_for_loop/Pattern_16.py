for i in range(6):
    for j in range(6):
        if i==0 or i==2 or i==4:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

print()

for i in range(6):
    for j in range(6):
        if i%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()