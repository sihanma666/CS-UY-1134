def split_parity(lst):
    for i in range(len(lst)):
        if(lst[i] % 2 != 0):
            lst.insert(0,lst.pop(i))
    return lst
        

test = split_parity([1,2,3,4])
print (test)
