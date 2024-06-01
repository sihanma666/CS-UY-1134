import ctypes;

def makearray(n):
    return (n * ctypes.py_object)();

class ArrayList:
    def __init__(self):
        self.data = makearray(1);
        self.capacity=1;
        self.n =0; #stored so we can avoid linear time calculation

    def __len__(self):
        return self.n;

    def append(self, item):
        if (self.n == self.capacity):
            self.resize(self.n*2);
            
        self.data[self.n] = item;
        self.n+=1;

    def extend(self, iterable_collection):
        if ((self.n+len(iterable_collection))>self.capacity):
            self.resize(self.n+len(iterable_collection));
        for item in iterable_collection:
            self.append(item);

    def resize(self, newsize):
        #make a new array
        newarray = makearray(newsize);

        #copy all of the old data over to the new array
        if (self.n>newsize):
            for i in range(newsize):
                newarray[i] = self.data[i];
            self.n=newsize;
        else:
            for i in range(self.n):
                newarray[i] = self.data[i];
                
        self.data = newarray; #make data point to the new array
        self.capacity=newsize;

    def __getitem__(self, index):
        if (index<0):
            index+=self.n;
        if (0<= index <= self.n-1):
            return self.data[index];
        raise IndexError("Invalid index");

    def __setitem__(self, index, value):
        if (index>=self.n):
            self.resize(index+1);
            for i in range(self.n,index):
                self.data[i] = None;
            self.n = index+1;
        if (0<= index <= self.n-1):
            self.data[index]=value;
        
    def __iter__(self):
        i=0;
        while(i<self.n):
            yield self.data[i]; #could instead yield self[i];
            i+=1;

                

def main():
    arr = ArrayList();
    arr.append(100);
    #arr.append(200);
    #arr[5] =100;
    for i in arr:
        print(i);
        #arr.append(arr[-1]+100); #Should cause an infinite loop
    #print(arr[100]);
    #print(arr[-1]);

if __name__=='__main__':
    main();
        
