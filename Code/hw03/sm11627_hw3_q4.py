#a The function is given a string s, and two indices: low and high (low <= high),
# which indicaate the range of indices that need to be considered.
# The function should return the number of lowercase letters at 
# the positions low, low+1,..., high in 

def count_lowercase(s, low, high):
    if(low > high or high > len(s)):
        raise IndexError
    elif(low == high):
        if (s.charAt(low)).islower():
            return 1
        else: return 0
    else:
        if (s.charAt(low)).islower():
            return 1 + count_lowercase(s, low-1, high)
        else: 
            return 0 + count_lowercase(s, low-1, high)


#b The function is given a string s, and two indices: low and high (low <= high), 
# which indicate the range of indices that need to be considered.
# The function should return True if there are even number of lowercase letters at
# the positions low, low+1, ..., high or False otherwise.

def is_number_of_lowercase_even(s, low, high):
    return count_lowercase(s, low, high) % 2 == 0
