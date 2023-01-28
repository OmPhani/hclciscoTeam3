from threading import *
import time
# print(threading.current_thread().getName())  OUTPUT : MainThread

def demo_thread():
    time.sleep(2)
    print("Hello")
demo_thread()

t1 = Thread(target = demo_thread)
t1.start()

