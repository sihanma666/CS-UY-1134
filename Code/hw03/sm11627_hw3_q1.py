import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n
    
    def insert(self, index, val):
        if not (-self.n <= index < self.n):
            raise IndexError('invalid index')

        if self.n == self.capacity: self.resize(self.capacity * 2)
        self.append(self[self.n-1])
        for i in range(self.n-1, index, -1):
            self[i] = self[i-1]
        self[index] = val
    
    def pop(self, index=-1):
        if not (-self.n <= index  and index <= self.n-1):
            raise IndexError('invalid index')
        elif self.n == 0:
            raise IndexError('empty list')

        x = self[index]

        index %= self.n
        for j in range(index, self.n-1):
            self[j] = self[j+1]
        self[self.n-1] = None
        self.n -= 1

        if self.n < self.capacity/4:
            self.resize(int(self.capacity/2))

        return x

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2*self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size

    def extend(self, iter_collection):
        for item in iter_collection:
            self.append(item)
