# Implement the function def findChange(lst01).
# This function is given lst01, a list of integers containing a sequence of 0s followed by a 
#sequence of 1s.
# When called, it returns the index of the first 1 in lst01.

# For example, if lst01 is a list containing [0,0,0,0,0,1,1,1], calling
# findChange(lst01) will return 5.

def findChange(lst01):
    left = 0
    right = len(lst01)-1 
    mid = int((left + right)/2)
    while(True): 
        if (mid > right):
            print(None)
            break
        if(lst01[mid] == 1 and lst01[mid-1] == 0):
            print(mid)
            break
        elif(lst01[mid]==1):
            mid -= 1
        else:
            mid += 1
        count += 1
    
def main():
    lst01 = [0,0,0,0,0,1,1,1]
    findChange(lst01)

main()

