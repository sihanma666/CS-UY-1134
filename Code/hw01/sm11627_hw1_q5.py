def two_sum(srt_lst, target):
    hi = len[srt_lst] - 1
    lo = 0
    while(lo < hi):
        total = srt_lst[hi] + srt_lst[lo]
        if(total == target):
            return (lo, hi)
        elif(total < target):
            hi -= 1
        elif(total > target):
            lo += 1
    return None