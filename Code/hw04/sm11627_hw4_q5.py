from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
import copy

def permutations(lst):
    permutation_queue = ArrayQueue()
    permutation_queue.enqueue([])
    itemS = ArrayStack()
    for i in range(len(lst)): 
        itemS.push(lst[i])

    while (itemS.is_empty() == False):
        item = itemS.pop()
        n = len(permutation_queue)
        for x in range(n):
            value = permutation_queue.dequeue()
            for i in range(len(value)+1):
                newP = copy.copy(value)
                newP.insert(i, item)
                permutation_queue.enqueue(newP)

    output = []
    while (permutation_queue.is_empty() == False):
        value = permutation_queue.dequeue()
        output.append(value)

    return output

def main():
    print(permutations([1,2,3]))

main()