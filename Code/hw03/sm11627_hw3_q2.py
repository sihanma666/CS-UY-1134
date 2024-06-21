# The remove(value) method of the list class, removes the first occurence of 
# value from the list it was called on, or raises a ValueError exception, if value is 
# not present.

# In this question we will look into the function remove_all(lst, value), that 
# removes all occurrences of value from lst.

#a worst-case run time: N^2
# def remove_all(lst, value):
#     end = False
#     while(end == False):
#         try:
#             lst.remove(value)
#         except ValueError:
#             end = True

#b Give implementation to remove_all that runs in worst-case linear time
#c worst-case runtime = 2N
def remove_all(lst, value):
    remove_lst = [0] * len(lst)
    for i in range(len(lst)):
        if (lst[i] == value):
            remove_lst[i] += 1
    for i in range(len(lst)):
        if (remove_lst[i] == 1):
            useless=lst.pop(i)
    return lst




