#    0 1 2 3 4 5
#   -5 -4 -3 -2 -1
a = [1,2,3,4,5,6]

print(a[0])
print(a[0:-1])     # prints from 0 to -1 
print(a[0: :2])   # print whole list from starting with gap 2
print(a[ : : 2])  # print whole list with gap 2

a = [i for i in range(1,10)]
print(a) 