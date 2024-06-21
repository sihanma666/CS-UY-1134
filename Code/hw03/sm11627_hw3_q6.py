
# The function is given a nested list of integers nested_list, and two indices: low and high
# (low <= high), which indicate the range of indices that need to be considered.

# The function should flatten the sub-list at the positions low, low+1, .., high of
# nested_list, and return this flattened lsit. That is, the function should create a new
# 1-level (non hierarchical) list that contains all the integers from the low...high range 
# in the input list.

# For example:
# nested_lst = [[1,2],3,[4,[5,6,[7],8]]] 
# flat_list(nested_lst, 0, 2)
# output: [1,2,3,4,5,6,7,8]

def flat_list(nested_lst, low, high):
    if (low > high):
        return []
    else:
        last_item = nested_lst[high]
        output = flat_list(nested_lst, low, high-1)
        if(isinstance(last_item, list)):
            temp = flat_list(last_item, 0, len(last_item)-1)
            output.extend(temp)
        else:
            output.append(last_item)7
        return output