import random 
import time

class Timer:
    def __init__(self):
        self.start = time.time()

    def reset(self):
        self.start = time.time()
    
    def elapsed(self):
        return (time.time() - self.start)

def find_index_of_min(ls, start, end):
    min_index = start
    for i in range(start+1, end):
        if(ls[i] < ls[min_index]):
            min_index = i
    return min_index

def selection_sort(lst): 
    #worst and best case theta N^2
    for current in range(len(lst)):
        min_index = find_index_of_min(lst, current, len(lst))
        lst[current],lst[min_index] = lst[min_index], lst[current]

def insertion_sort(ls):
    # worst case Theta: N^2
    # best case Theta: N
    # average case Theta: N^2
    for i in range(i, len(ls)):
        value = ls[i]
        j = 0
        while(j>0 aand ls[j]>value):
            ls[j] = ls[j-1]
            j-=1
        ls[j] = value

def merge_sort(): 
    #Theta: N * log(N)
    def merge(ls, left_ind, left_end, right_end, temp):
        # Theta: N
        # RUNTIME: <=2n 
        right_ind = left_end+1
        temp_ind = left_ind
        original_start = left_ind
        while((left_ind<=left_end) and (right_ind<right_end)):
            if(ls[left_ind]<ls[right_ind]):
                temp[temp_ind]=ls[left_ind]
                temp_ind+=1
                left_ind+=1
            else:
                temp[temp_ind] = ls[right_ind]
                temp_ind+=1
                right_ind+=1
        while(left_ind<=left_end): #will run one
            temp[temp_ind]=ls[left_ind]
            temp_ind+=1
            left_ind+=1
        while(right_ind<=right_end):
            temp[temp_ind]=ls[right_ind] #or another
            temp_ind+=1
            right_ind+=1
        while (original_start<=right_end):
            ls[original_start]=temp[original_start]
            original_start+=1

    def merge_sort(ls, start, end, temp):
        if (start<end):
             mid = (start+end)//2
             merge_sort(ls,start,mid,temp)
             merge_sort(ls,mid,end,temp)
             merge(ls,start,mid,end,temp)

    temp_ls=[]
    temp_ls.extend(ls) 
    merge_sort(ls,0,len(ls)-1, temp_ls)

def quick_sort(ls):
    # Theta: N
    # if bad pivot wrongly chosen. can make theta approach N^2
    def quick_sort(ls, start, end):
        if(end<(start+10)):
            insertion_sort(ls,start,end)
            return
        center = (start+end)//2
        if(ls[center]<ls[start]):
            ls[center], ls[start] = ls[start], ls[center]
        if(ls[end]<ls[start]):
            ls[end], ls[start] = ls[start], ls[end]
        if(ls[end]<ls[center]):
            ls[center], ls[end] = ls[end], ls[center]
        
        pivot = ls[center]
        ls[center],ls[end-1] = ls[end-1], ls[center]
        i=start+2
        j=end-2
        while(True):
            while(ls[i]<pivot):
                i+=1
            while(ls[j]>pivot):
                j-=1
            if(i<j):
                ls[i],ls[j]=ls[j],ls[i]
            else:
                break
        ls[end-1],ls[i] = ls[i], ls[end-1]
        quick_sort(ls,start,i-1)
        quick_sort(ls, i+1, end)

    quick_sort(ls,0,len(ls-1))
    

def main():
    ls=[]
    count = 1000
    t = Timer()
    for j in range(10):
        for i in range(count):
            ls.append(random.randint(1,1000000))
        t.reset()
        selection_sort(list)
        elapsed = t.elapsed()
        print("Sorting", len(ls), "elements took", elapsed, "seconds")

main()
    

                    
    