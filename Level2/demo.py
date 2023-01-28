import multiprocessing as mp
import math
import time

from time import time, perf_counter

r1 = []
r2 = []

def cal_one(number):
    for i in number:
        r1.append(math.sqrt(i**3))

def cal_two(number):
    for i in number:
        r2.append(math.sqrt(i**5))

if __name__ == '__main__':
    numlist = list(range(2500000))
    p1 = mp.Process(target = cal_one,args = (numlist,))
    p2 = mp.Process(target=cal_one, args=(numlist,))
    start = perf_counter()
    p1.start()
    p2.start()
    end = perf_counter()
    print(f'{end-start} seconds taken')

cal_one(2)
cal_two(3)