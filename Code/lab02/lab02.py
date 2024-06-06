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
    for i in range(int(len(list_str))/2):
        high_vowel = False
        low_vowel = False

        if (low >= high):
            break
        elif ((high == 'a') or (high == 'e') or (high == 'i') or (high == 'o') or (high == 'u')):
            high_vowel = True
        elif ((low == 'a') or (low == 'e') or (low = 'i') or (low == 'o') or (low == 'u')):
            low_vowel = True

        if (high_vowel == True and low_vowel == True):
            temp_str = list_str[low]
            low = list_str[high]
            list_str[high] = temp_str
            low += 1
            high -= 1

        elif (high_vowel == True):
            low += 1
        elif (low_vowel == True):
            high -= 1
    return "".join(list_str)
