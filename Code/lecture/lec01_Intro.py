import math;
import time;
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to_origin(self):
        return ((self.x*self.x)+(self.y*self.y))**0.5
    def get_distance(self, other):
        delta_x = self.x-other.x
        delta_y = self.y-other.y
        return math.sqrt((delta_x**2)+(delta_y**2))
    
def find_closest_pair(points): #Theta: N^2
    min_distance = points[0].get_distance(points[1])
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = points[i].get_distance(points[j])
            if ( dist < min_distance):
                min_distance = dist
    return min_distance
def demo1(n):
    count=0
    for i in range(n):
        for j in range(n):
            if (i==j):
                for k in range(n):
                    count+=1
    print(count)


def closest_point_to_origin(points): # Theta: N
    min_index = 0
    for i in range(1,len(points)):
        if (points[i].distance_to_origin() < points[min_index].distance_to_origin()):
            min_index = i
    return points[min_index];        

class Timer:
    def __init__(self):
        self.start = time.time()
    def reset(self):
        self.start = time.time()
    def elapsed(self):
        return (time.time() - self.start)

def fib(n): #n=4, fib(3) + fib(2), (fib(2)+fib(1)) + (fib(1)+fib(0)), (1+1) + (1+1), 4
    if (n<=2):
        return 1
    return fib(n-1) + fib(n-2)

def mcss1(vals): #Theta: N^3
    max_sum = 0
    for i in range(len(vals)):
        for j in range(i,len(vals)):
            sum = 0
            for k in range(i,j+1):
                sum+=vals[k]
            if (sum>max_sum):
                max_sum = sum
    return max_sum

def mcss2(vals): #Theta: N^2
    max_sum = 0
    for i in range(len(vals)):
        sum = 0
        for j in range(i, len(vals)):
            sum+=vals[j]
            if (sum>max_sum):
                max_sum = sum
    return max_sum

def mcss3(vals): #Theta: N
    max_sum = 0
    sum = 0
    for i in range(len(vals)):
        sum+=vals[i]
        if sum>max_sum:
            max_sum = sum
        elif sum<0:
            sum = 0
    return max_sum

# def main():
#     points=[Point(5,4), Point(3,2), Point(1,1), Point(-1,0), Point(13,12)]
#     demo1(10)

#    t = Timer()
#    for i in range(100):
#        t.reset()
#        val = fib(i)
#        elapsed = t.elapsed()
#        print("fib(",i,")=",val,"that took",elapsed,"seconds")

# if __name__=='__main__':
#     main()
