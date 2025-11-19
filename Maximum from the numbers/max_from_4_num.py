a = int(input("Enter the value for a : ")) 
b = int(input("Enter the value for b : "))
c = int(input("Enter the value for c : "))
d = int(input("Enter the value for d : "))

if a>b and a>c and a>d:
    print(a,"is maximum than d ",d,b,"and",c)
elif b>a and b>c and b>d:
    print(b,"is maximum than d ",d,a,"and",c)
elif c>a and c>b and c>d:
    print(c,"is maximum than d ",c,a,"and",b)
else:
    print(d,"is maximum than c ",d,a,"and",b)