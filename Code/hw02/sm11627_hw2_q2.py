# Implement a function def factors(num). This function is given a positive integer
# num, and returns a generator, that when iterated over, it will have all of num's divisors
# in an ascending order.

# For Example, if we execute the following code:
#     for curr_factor in factors(100):
#         print(curr_factor)
# The expected output is:
# 1 2 4 5 10 20 25 50 100

import math

def factors(num): #Theta: sqrt(N) 
    ls_1, ls_2 = [], []
    i = 1
    mid_count = 0
    max = math.sqrt(num) 
    while(i<=max): 
        if(num % i == 0):
            if(i != max):
                ls_1.insert(mid_count, i) 
                mid_count += 1 
                ls_1.insert(mid_count, int(num/i)) 
            else:
                ls_1.insert(mid_count, i)
        i += 1
    return ls

def main():
    print('main')
    for curr_factor in factors(24): #
        print(curr_factor)

main()

# QUESTIONS: 
# Is it fine that the print output does not happen in the same line like shown above