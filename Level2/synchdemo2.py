from threading import *
import time
l = Lock()
def wish(name):

    l.acquire()
    for i in range(3):
        print("Good Evening", end = " ")
        time.sleep(2)
        print(name)
    l.release()

bt = time.time()
t1 = Thread(target = wish,args=("jose",))
t2 = Thread(target = wish,args=("mich",))
t3 = Thread(target = wish,args=("mart",))
"""
t1.start()
t1.join()
t2.start()
t2.join(1)
t3.start()
t3.join()
"""

t1.start()
t2.start()
t3.start()
print(time.time()-bt,sep= " ")


