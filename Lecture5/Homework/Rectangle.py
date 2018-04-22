class Rectangle(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def s(self):
        return self.a * self.b

    def p(self):
        return (self.a + self.b) * 2


if __name__ == '__main__':
    r1 = Rectangle(4, 6)
    print('Square is:', r1.s())
    print('Perimeter is:', r1.p())

    r2 = Rectangle(5, 8)
    print('\nSquare is:', r2.s())
    print('Perimeter is:', r2.p())
