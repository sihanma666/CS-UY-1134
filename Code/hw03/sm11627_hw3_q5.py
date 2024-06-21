# The function is given a list lst of non-zero itnegers, and two indices: low and high 
# (low <= high), which indicate the range of indices that need to be considered.
# The function should reorder the elements in lst, so that all the negative numbers
# would come before all the positive numbers.

def split_by_sign(lst, low, high):
    if(low>=high):
        return lst
    if(lst[low]<0): 
        if(lst[high]>=0):
            split_by_sign(lst, low+1, high-1)
        else:#(lst[high]<0):
            split_by_sign(lst, low+1, high)
    else:#(lst[low]>=0):
        if(lst[high]>=0):
            split_by_sign(lst, low, high-1)
        else:#(lst[high]<0): #both in wrong place
            lst[low], lst[high] = lst[high], lst[low]
            split_by_sign(lst, low+1, high-1)
