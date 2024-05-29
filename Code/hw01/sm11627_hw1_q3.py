#You are given an implementation of a Vector class, representing the coordinates of a vector
#in a multidimensional space. For example, in a three-dimensional space, we might wish to 
#represent a vector with coordinates <5,-2,3>.

class Vector:
    def __init__(self, d):
        self.coords = [0] *d

    def __init__(self, lst):
        self.coords = []
        for i in range(len(lst)):
            self.coords.append(i)

    def __len__(self):
        return len(self.coords)
    
    def __getitem__(self, j):
        return self.coord[j]
    
    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions don't match")
        resultLst = Vector(len(self))
        for i in range(len(self)):
            resultLst[i] = self[i] - other[i]
        return resultLst
    
    def __neg__(self):
        resultLst = Vector(len(self))
        for i in range(len(self)):
            resultLst[i] = -1 * self[i]
        return resultLst
    
    def __mul__(self, other):

        if isinstance(other, int):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = other * self[j]
            return result
        else:
            if (len(self) != len(other)):
                raise ValueError("dimensions must agree")
            result = 0
            for j in range(len(self)):
                result += self[j] * other[j]
            return result

    def __rmul__(self, other):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other * self[j]
        return result
    
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __ne__(self, other):
        return not (self == other)
    
    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'
    
    def __repr__(self):
        return str(self)