
#a. Demonstrate how to use Python's list comprehension syntax to produce the list:
#[1,10,100,1000,10000,100000]

def listComprehension_A(n):
    newList = []
    for i in range(n):
        newList.append(10**(i-1))
    return newList

#b. Demonstrate how to use Python's list comprehension syntax to produce the list:
#[0,2,6,12,20,20,42,56,72,90]

def listComprehension_B(n):
    newList = [0]
    sum=0
    for i in range(n):
        sum += 2**i
        newList.append(sum)
    return newList

#c. Demonstrate how to use Python's list comprehension syntax to produce the list
#['a','b','c',...,'z'], but without having to type all 26 such characters literally

def listComprehension_C():
    newList = []
    for i in range(97, 112):
        newList.append(chr(i))
    return newList



def main():
    print ("hello")
    print (listComprehension_A(3))

    lst1 = [1,2,3]
    lst2 = [lst1 for i in range(3)]
    lst2[0][0] = 10
    print(lst2)
    print(lst1)

main()
