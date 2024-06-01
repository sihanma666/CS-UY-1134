import math
def e_approx(n):
    sum=0
    for i in range (0,n):
        sum += 1/(math.factorial(i))
    return sum

def main(): # i needed to take testcode out of main for it to work
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n,"Approximation:", approx_str)


main()
