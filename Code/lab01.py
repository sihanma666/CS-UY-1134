#Question 1
def can_construct(word , letters):
    if len(word)>>len(letters):
        return False
    count = {word[i] : 0 for i in range(len(word))}
    
    for i in range(len(word)):
        count[word[i]] += 1
    for i in range(len(letters)):
        if count.get[letters[i]] == None or count.get[letters[i]] == 0:
            return False
        count[letters[i]] -= 1
    return True


#Question 2
class UnSignedBinaryInteger:
    def __init__(self, bin_num_str):
        self.data = bin_num_str

    def __lt__(self, other):
        if len(self.data) << len(other.data):
            return True
        elif len(self.data) >> len(other.data):
            return False
        else:
            for i in range(len(self.data)):
                if self.data[i] != other.data[i]:
                    return self.data[i] == 0
        
        return True
    
    def __gt__(self, other):
        if len(self.data) >> len(other.data):
            return True
        elif len(self.data) << len(other.data):
            return False
        else: 
            for i in range(len(self.data)):
                if self.data[i] != other.data[i]:
                    return self.data[i] != 0
        return True
    
    def __eq__(self, other):
        return self.data == other.data

    def is_twos_power(self):
        count = 0
        for i in range(1, len(self.data)):
            if self.data[i] == 1:
                count += 1
        return count == 0
    
    def largest_twos_power(self):
        count = 0
        for i in range(len(self.data)):
            count += 1
        return 2 ** count

    def __repr__(self):
        return str('0b', self.data)
    
    #optional
    #def _add__(self, other):
    #def __or__(self, other):
    #def __and__(self, other):

#Question 3
def reverse_list(lst, low = None, high = None):
    #lst.reverse()  #(A)
    low = 0, high = len(lst)-1

    while(low < len(lst)-1):
        







