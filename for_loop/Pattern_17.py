#       - 1 + 2 - 3 + 4 - 5 + 6 - .........N

for i in range(1,7):
    if i==6:
        print("+",i,end=" - .........N") 
    elif i%2==0:
        print("+",i,end=" ")
    else:
        print("-",i,end=" ")

print()

for i in range(1,7):
    if i==1:
        print("-",i,end=" + ")
    elif i==6:
        print(i,end=" - .........N")
    elif i%2==0:
        print(i,end=" - ")
    else:
        print(i,end=" + ")