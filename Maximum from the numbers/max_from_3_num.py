a = int(input("Enter the value for a : ")) 
b = int(input("Enter the value for b : "))
c = int(input("Enter the value for c : "))


if a>b and a>c:
    print(a,"is maximum than both ",b,"and",c)
elif b>a and b>c:
    print(b,"is maximum than both ",a,"and",c)
else:
    print(c,"is maximum than both ",a,"and",b)