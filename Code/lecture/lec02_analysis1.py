import random;
import time;

class Timer:
    def __init__(self):
        self.start = time.time();
    def reset(self):
        self.start = time.time();
    def elapsed(self):
        return (time.time() - self.start);



def main():
    ls = [];
    increment=1000000;
    t = Timer();
    size = 0;
    for i in range(10):
        ls.clear();
        size+=increment;
        for i in range(size):
            ls.append(random.randint(0,10000000));
        t.reset();
        ls.sort();
        elapsed = t.elapsed();
        print("Sorting with",size,"elements took",elapsed,"seconds");



if __name__=='__main__':
    main();
