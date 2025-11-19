def fibonacci(x):
    a = -1
    b =  1
    for i in range(0,x):
        c = a + b
        print(c,end=" ")
        a = b
        b = c

n = int(input("Enter the number till you want fibonacci series : "))
fibonacci(n)

