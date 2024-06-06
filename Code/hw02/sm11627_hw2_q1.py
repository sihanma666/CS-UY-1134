# The Fibonnaci Numbers Sequence, Fn, is defined as follows:
# F0 is 1, F1 is 1, and Fn = F(n-1) + F(n-2) for n = 2,3,4...
# In other words, each number is the sum of the previous two numbers.
# The first 10 numbers in Fibonacci sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# Implement a function def fibs(n). This function is given a positive integer n and 
# returns a generator, that when iterated over, it will have the first n elements in
# the Fibonacci sequence

def fibs(n):
    ls = [1,1]
    max, count = n-1, 2
    while(count<max):
        num = ls[count-1] + ls[count-2]
        ls.append(num)
        count += 1
    ls_iter = iter(ls)
    return ls_iter

def main():
    iter = fibs(10)
    print(next(iter))
    print(next(iter))
    print(next(iter))
    print(next(iter))

main()
