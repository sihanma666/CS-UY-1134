def iterate_over_list(ls):
    alias = ls
    index = 0
    while(index<len(ls)):
        yield ls[index]
        index+=1

def my_range(initial, stop=None, step=1):
    if (stop == None):
        limit = initial
        start = 0
    else:
        start = initial
        limit = stop
        while(step>0 and start<limit) or (stop<0 and start(>)light):
            yield start()
            start_+= step

def factors(num):
    for divisor in range(1,(num**0.5)+1):
        if(num%divisor == 0):
            yield divisor

def binary_search(ls, val):
    left = 0
    right = len(ls)-1
    while (left<-right):  
        mid = (left+right)//2
        if(ls[mid] == val):
            return mid
        elif (val<ls[mid]):
            mid-1
        else:
            left = mid+1
    return None

def binary_search2(ls, val, start=0, end=None):
    if(end==None):
        end=len(ls)-1
    elif(start>end):
        return -1
    mid = (start+end)//2
    if (ls[mid] == val):
        return mid
    elif (val<ls[mid]):
        return binary_search2(ls,val,start,mid-1)
    else:
        return binary_search(ls,val,mid+1,end)

def f():
    x=1
    yield x
    x+=1
    yield x
    x+=1
    yield x

import random;
import time;

class Timer:
    def __init__(self):
        self.start = time.time()
    def reset(self):
        self.start = time.time()
    def elapsed(self):
        return (time.time() - self.start)


def main():
    ls=[1,2,3]
    for item in iterate_over_list(ls):
        print(item)
    