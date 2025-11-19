def fibonacci(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else :
        return fibonacci(n-1) + fibonacci(n-2)

n = 5
for i in range(0,n):
    print(fibonacci(i))


# i           n                 o/p
# 0           0                  0
# 1           1                  1
# 2           (2-1)  + (2-2)      1
# 3           (3-1)  + (3-2)      
#             fib(2) + fib(1)   
#               1    + 1         2
