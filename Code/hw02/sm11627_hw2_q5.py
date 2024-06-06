# a. Write a function def shift(lst, k) that is given a list of N numbers and some
# positive integer k (where k<N). The function should shift the numbers circularly k steps to the left.range

# The shift has to be done in-place. That is, the numbers in the parameter list should
# reorder to form the correct output (you shouldn't create and return a new list with the
# shifted result).

# For example, if lst = [1,2,3,4,5,6]
# after calling shift(lst, 2).
# lst will be [3,4,5,6,1,2]

# b. Modify your implementation, so we could optionally pass to the function a third
# argument that indicates the direction of the shift (either 'left' or 'right').

# note: cant use pop or insert

def shift_a(lst, k):
    for i in range(len(lst)):
        if(i<k):
            lst.append(lst.pop(0))
    return lst

def shift(lst, k, str):
    if(str == 'left'):
        for i in range(len(lst)):
            if(i<k):
                lst.append(lst.pop(0))
    elif(str == 'right'):
        k_inv = len(lst)-k
        for i in range(len(lst)):
            if(i<k_inv):
                lst.append(lst.pop(0)) #[561234]
    else:
        print('third parameter must be left or right')
    return lst
                      
def main():
    lst = [1,2,3,4,5,6]
    lst_iter = iter(shift(lst, 2, 'right'))
    for i in range(len(lst)):
        print(next(lst_iter))
main()