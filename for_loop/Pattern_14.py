#    1 + 2 + 3 + 4 + 5 =
for i in range(1,6):
    if i==5:
        print(i,end=" =")
    else:
        print(i,end=" + ")

print()

for i in range(1,6):
    if i==5:
        print(i,end=" =")
    else:
        print(i,"+",end=" ")