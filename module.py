# module模块

print('enter module ...')

name = 'Welcome'

def add(l, r):
    if type(l) is not type(r):
        print('l and r must be the same type')
        return None
    return l + r

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%.2f, %.2f)' % (self.x, self.y)
    def __repr__(self):
        return 'Point(%.2f, %.2f)' % (self.x, self.y)
    def __call__(self):
        return self.__str__()


class Circle:
    def __init__(self, o, radius):
        self.o = o
        self.radius = radius


print('module end...')