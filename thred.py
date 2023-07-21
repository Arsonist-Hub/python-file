import threading
import time

print(threading.active_count())

a = []

def count():
    for i in range (0,5):
        a.append(i)
        time.sleep(0.5)

def count2():
    for j in range (0,5):
        a.append(j)
        time.sleep(0.5)

x = threading. Thread(target=count)
y = threading. Thread(target=count2)

x.start()
y.start()
print(threading.active_count())

x.join()
y.join()
print(threading.active_count())
print (a)





