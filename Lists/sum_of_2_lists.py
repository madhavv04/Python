# SUm of two lists elements like 1 + 5 , 2 + 6 ....
a = [1,2,3,4]
b = [5,6,7,8]
c = [0,0,0,0]

for i in range(len(a)) :
    c[i] = a[i] + b[i]
    print(c[i])
    
