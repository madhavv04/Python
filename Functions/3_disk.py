def disk1():
    print("Enter in disk 1")
    print("Exit from disk 1")

def disk2():
    print("Enter in disk 2")
    disk1()
    print("Exit from disk 2")

def disk3():
    print("Enter in disk 3")
    disk2()
    print("Exit from disk 3")

disk3()



#   disk3 ----> disk2 ----> disk1---|
#   ^             ^                 |
#   |             |                 | 
#   ---------------------------------