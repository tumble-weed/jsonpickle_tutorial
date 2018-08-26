import numpy as np

class a():
    def __init__(self):
        self.nparray = np.random.random(size=(100,))
        self.string = 'This is class a'

class b():
    def __init__(self):
        self.string1 = 'Wont find an array here, bub'
        self.string2 = 'This is class b'

__all__ = ['a','b']