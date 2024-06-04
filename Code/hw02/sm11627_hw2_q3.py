# Define a generator that takes in a number n and returns the powers of 2 up to n:
# def powers_of_two(n)
    
# For example:
# powers_of_two(6)
# will return 
# 1, 2, 4, 8, 16, 32

def powers_of_two(n):
    ls = []
    i = 0
    while (i < n):
        ls.append(2**i)
        i += 1
    #ls_iter = iter(ls)
    print(ls)

def main():
    powers_of_two(6)
    print('main')

main()