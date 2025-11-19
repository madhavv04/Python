
a = [1,2,3,4]
b = [5,6,7,8]
c = [0,0,0,0,0,0,0,0]
counter = 0
for i in range(len(a)) :
    c[i] = a[i]
    counter+=1 
    

for i in range(len(b)):
    c[counter] = b[i]
    counter+=1


print(c)
