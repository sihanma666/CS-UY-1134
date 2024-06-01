
def iterate_over_list(ls):
    alias = ls;
    index = 0;
    while (index<len(ls)):
        yield ls[index];
        index+=1;

def binary_search1(ls,val):
    left = 0;
    right = len(ls)-1;
    while (left<=right):
        mid = (left+right)//2;
        if (ls[mid] == val):
            return mid;
        elif (val<ls[mid]):
            right=mid-1;
        else:
            left=mid+1;
    return None;

def binary_search2(ls, val,start=0, end=None):
    if (end==None):
        end=len(ls)-1;
    elif (start>end):
        return None;
    mid = (start+end)//2;
    if (ls[mid] == val):
        return mid;
    elif(val<ls[mid]):
        return binary_search2(ls,val,start, mid-1);
    else:
        return binary_search2(ls,val,mid+1, end);


def f():
    x=1;
    yield x;
    x+=1;
    yield x;
    x+=1;
    yield x;

def my_range(initial, stop=None, step=1):
    if (stop==None):
        start = 0;
        limit = initial;
    else:
        start = initial;
        limit = stop;
    while ((step>0 and start<limit) or (step<0 and start>limit)):
        yield start;
        start+=step;

def factors(num):
    for divisor in range(1,int(num**0.5)):
        if (num%divisor==0):
            yield divisor;
            #yield num//divisor;
    for divisor in range(int(num**0.5)+1,0,-1):
        if (num%divisor==0):
            yield num//divisor;

def main():
    for i in factors(28):
        print(i);
#    ls=[1,2,3];
#    for item in iterate_over_list(ls):
#        print(item);
##    gen = f();
##    print(next(gen));    
##    print(next(gen));    
##    print(next(gen));    
##    print(next(gen));    

##ls=[1];
##for i in ls:
##    ls.append(i+1);
##    print(i);
##print("done");
    

##ls = list(range(1,11));
##for i in ls:
##    print(i);
##    ls.pop(0);
##print("Done");
##
##s = "abc";
##for item in s:
##    print(item);
##    
##s = "abc";
##s_iter = iter(s);
##

if __name__=='__main__':
    main();
