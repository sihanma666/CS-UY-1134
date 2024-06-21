#1
def is_palindrome(s):
    mid_constant = int(len(s)/2)
    left, right = mid_constant, mid_constant
    if(len(s) % 2 == 1): #odd str length
        for i in range(mid_constant):
            left -= 1
            right += 1
            if(s[left] != s[right]):
                return False
    elif(len(s) % 2 == 0 and s[mid_constant] == s[mid_constant-1]):
        left = mid_constant - 1
        for i in range(mid_constant - 1):
            left -= 1
            right += 1
            if(s[left] != s[right]):
                return False
    else:
        return True
    
#2
def reverse_vowels(input_str):
    list_str = list(input_str)
    low = 0
    high = len(list_str)-1
    vowels = 'aeiou'
    for i in range(int(len(list_str))/2):
        high_vowel = False
        low_vowel = False

        if (low >= high):
            break
        elif (list_str[high] in vowels):
            high_vowel = True
        elif (list_str[low] in vowels):
            low_vowel = True

        if (high_vowel == True and low_vowel == True):
            list_str[low], list_str[high] = list_str[high], list_str[low]
            low += 1
            high -= 1
        elif (high_vowel == True):
            low += 1
        elif (low_vowel == True):
            high -= 1
    return "".join(list_str)

#3
import math

def find_missing(lst):
    #a. worst case run-time: N^2
    # for num in range(len(lst)+1):
    #     if num not in lst:
    #         return num
    #b. hINT: compare value to index
    left = 0
    right = len(lst) - 1

    if len(lst) == 0: 
        return 0
    if lst[right] == len(lst) - 1:
        return len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] != mid:
            right = mid
        else:
            left = mid + 1
    return left

#def find_missing_c(lst):
    # find sum of whole list, find actual sum of list
    # subtract to find missing number

#4
def find_pivot(lst):
    left = 0
    right = len(lst)-1
    for i in range(len(lst)):
        if lst[i+1] < lst[i]:
            return i
    return None

