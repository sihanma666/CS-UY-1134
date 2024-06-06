def countdown(n):
    if (n <= 0):
        return
    print(n)
    countdown(n-1)

def countup(n):
    if(n<=0):
       return
    countup(n-1)
    print(n)

def countup2(start,limit):
    if(start>=limit):
        return
    countup(start, limit-1):
    print(limit-1)

def countup3(start, limit):
    if(start>limit):
        return
    elif(start==limit):
        print(start)
    else:
        mid = (start+limit)
        countup3(start,mid)
        countup3(mid+1,limit)

def count_up_and_down(n):
    if(n==1):
        print(1)
        return
    print(n)
    count_up_and_down(n-1)
    print(n)

def list_sum(ls):
    if(len(ls)==0):
        return 0
    else:
        return ls(0) + list_sum(ls[1:])#slicing costs N^2 bc n lists created

def list_sum2(ls):
    if(len(ls)==0):
        return 0
    temp = ls.pop()
    sub_sum = list_sum2(ls)
    ls.append(temp)
    return sub_sum+temp

def list_sum3(ls, ptr=0):
    if (ptr==len(ls)):
        return 0
    return ls[ptr]+list_sum3(ls, ptr+1)

def list_sum4(ls):
    def list_sum_helper(ls, ptr):
        if(ptr==len(ls)):
            return 0
        return ls[ptr] + list_sum3(ls, ptr+1)
    return list_sum_helper(ls,0)

def count_appearnaces(ls, val):
    def count_appearance_helper(ls, val, low, high):
        if(low<=high):
            if(ls[low] == val):
                return 1+count_appearance_helper(ls, val, low+1, high)
            else:
                return count_appearance_helper(ls, val, low+1, high)
        else:
            return
    count_appearance_helper(ls, val, 0, len(ls)-1)# runtime = 10

def power(base, exp):
    if(exp==0):
        return 1
    else:
        return base * power(base, exp-1)
    
def fast_power(base, exp): #runtime: N
    if(exp==1):
        return base
    elif(exp == 0):
        return 1
    else:
        part1 = fast_power(base, exp//2)
        part2 = fast_power(base, exp//2)
        if(exp%2==0):
            return part1*part2

def really_fast_power(base, exp): #runtime: log(N)
    if(exp==1):
        return base
    elif(exp == 0):
        return 1
    else:
        part1 = really_fast_power(base, exp//2)
        if(exp%2==0):
            return part1*part1
        
def pos_ints_list(n):
    
    
    

def main():
    countdown(5)

if __name__=='__main__':
    main()