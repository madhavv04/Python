from threading import Thread,current_thread
import time

# threading.Thread
def method1():
    print("welcome in mwthod1")
    print(current_thread().name)
    time.sleep(1)
    print("Bye from mwthod1")

def method2():
    print("welcome in method2")
    print(current_thread().name)
    time.sleep(1)
    print("Bye from method2")

def method3():
    print("welcome in method3")
    print(current_thread().name)
    time.sleep(1)
    print("Bye from method3")

t1 = Thread(target=method1)
t2 = Thread(target=method2)
t3 = Thread(target=method3)

t1.start()
t2.start()
t3.start()
print(current_thread().name)