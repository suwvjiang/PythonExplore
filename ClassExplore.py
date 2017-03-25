#student类
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name :%s)'%self.name
    __repr__ = __str__
    def __getattr__(self, attr):
        raise AttributeError('\'Student\' Object has no attribute:\'%s\'' % attr)

#斐波那契数
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 10000000:
            raise StopIteration()
        return self.a
    
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b, a+b
            return L

import os

def main():
    fib = Fib()
    print fib[0:10]

    #s = Student('jiang')
    #print s.score
    print os.name
main()