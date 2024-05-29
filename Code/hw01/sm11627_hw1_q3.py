#You are given an implementation of a Vector class, representing the coordinates of a vector
#in a multidimensional space. For example, in a three-dimensional space, we might wish to 
#represent a vector with coordinates <5,-2,3>.

class Vector:
    def __init__(self, d):
        self.coords = [0] *d
    def __init__(self, x, y, z):
        self.coords.append(x)
        self.coords.append(y)
        self.coords.append(z)

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
    
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __ne__(self, other):
        return not (self == other)
    
    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'
    
    def __repr__(self):
        return str(self)