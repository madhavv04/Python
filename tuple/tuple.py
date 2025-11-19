a = [(1,2),(3,4)]
a[0][0] = 0
print(a)

#      0     1     2
#     0 1   0 1   0  1
b = ([1,2],[3,4],[5,0])
print(b)

b[0][0] = 0 # Changing value of list 1 at index 0
b[0][1] = 1 # Changing value of list 1 at index 1
b[1][0] = 2 # Changing value of list 2 at index 0
b[1][1] = 3 # Changing value of list 2 at index 1
b[2][1] = 3 # Changing value of list 2 at index 1


print(b)



# a = ([1,2],[3,4])
# print(a)

# a[0][0]=2
# a[0][1]=2
# print(a)