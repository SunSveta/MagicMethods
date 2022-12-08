
class MyInt:
    def __init__(self, val):
        self.val = val

    @classmethod
    def verify(cls, other):
        if isinstance(other, (str, int)):
            return int(other)


    def __repr__(self):
        return f'{self.__class__} : {self.val}'

    def __str__(self):
        return f'{self.val}'

    def __add__(self, other):
        other = self.verify(other)
        return MyInt(self.val + other)

    def __sub__(self, other):
        other = self.verify(other)
        return MyInt(self.val - other)

    def __mul__(self, other):
        other = self.verify(other)
        return MyInt(self.val * other)

    def __truediv__(self, other):
        other = self.verify(other)
        return MyInt(self.val / other)

    def __eq__(self, other):
        other = self.verify(other)
        return self.val == other

    def __lt__(self, other):
        other = self.verify(other)
        return self.val < other

    def __le__(self, other):
        other = self.verify(other)
        return self.val <= other

    def __gt__(self, other):
        other = self.verify(other)
        return self.val > other

    def __ge__(self, other):
        other = self.verify(other)
        return self.val >= other

a = MyInt(10)