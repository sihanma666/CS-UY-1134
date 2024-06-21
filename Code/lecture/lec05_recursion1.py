

def countdown(n):
    if (n<=0): #The base case
        return;
    print(n); #The simple case
    countdown(n-1); #Reduction of the set by the simple case

def countup(n):
    if (n<=0):
        return;
    countup(n-1);
    print(n);

def countup1(start, limit):
    if (start>=limit):
        return;
    print(start);
    countup1(start+1,limit);

def countup2(start, limit):
    if (start>=limit):
        return;
    countup2(start,limit-1);
    print(limit-1);

def countup3(start, limit):
    if (start>limit):
        return;
    elif (start==limit):
        print(start);
    else:
        mid = (start+limit)//2;
        countup3(start,mid);
        countup3(mid+1, limit);


def count_down_and_up(n):
    if (n==1):
        print(n);
    else:
        print(n);
        count_down_and_up(n-1);
        print(n);

def list_sum(ls): #Theta: N^2
    if (len(ls)==0):
        return 0;
    return ls[0] +list_sum(ls[1:]);

def list_sum2(ls): #Theta: N (ish)
    if (len(ls)==0):
        return 0;
    temp = ls.pop();
    sub_sum = list_sum2(ls);
    ls.append(temp);
    return sub_sum+temp;

def list_sum3(ls, ptr=0):
    if (ptr ==len(ls)):
        return 0;
    return ls[ptr]+list_sum3(ls, ptr+1);

def list_sum4(ls):
    def list_sum_helper(ls, ptr):
        if (ptr ==len(ls)):
            return 0;
        return ls[ptr]+list_sum3(ls, ptr+1);
    return list_sum_helper(ls,0);


def count_appearances(ls, val):
    def count_appearances_helper(ls, val, low, high):
        if (low<=high):
            if (ls[low] == val):
                return 1+count_appearances_helper(ls, val, low+1, high);
            else:
                return count_appearances_helper(ls, val, low+1, high);
        else:
            return 0;
    count_appearances_helper(ls, val, 0, len(ls)-1);

def power(base, exp): #Theta: n (exp)
    if (exp==0):
        return 1;
    else:
        return power(base,exp-1)*base;

def fast_power(base, exp): #theta:N
    if (exp==1):
        return base;
    elif (exp==0):
        return 1;
    else:
        part1 = fast_power(base, exp//2);
        part2 = fast_power(base, exp//2);
        if (exp%2==0):
            return part1*part2;
        else:
            return base*part1*part2;

def really_fast_power(base, exp): #theta: log n
    if (exp==1):
        return base;
    elif (exp==0):
        return 1;
    else:
        part1 = fast_power(base, exp//2);
        part2 = part1;
        if (exp%2==0):
            return part1*part2;
        else:
            return base*part1*part2;
def pos_ints_list(n):
    if (n<=0):
        return [];
    else:
        res_list = pos_ints_list(n-1);
        res_list.append(n); #constant -ish
        #res_list=res_list +[n]; #linear!!!!
        return res_list;

def powers_of_2_list(n):
    if (n<=1):
        return [1];
    else:
        res_list=powers_of_2_list(n-1);
        #next_power = really_fast_power(2,n); #log n
        next_power = res_list[-1]*2; #constant
        res_list.append(next_power);
        return res_list;

def main():
    countup(5);

if __name__=='__main__':
    main();
