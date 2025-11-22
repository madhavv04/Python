from threading import Thread
import time

def method():
    for i in range(1,6):
        time.sleep(2)
        print(i)

t1 = Thread(target=method)

t1.start()

for i in range(10,51,10):
    time.sleep(1)
    print(i)