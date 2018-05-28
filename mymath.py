import math


class Vect:
    def __init__(self, ax, ay):
        self.x = ax
        self.y = ay

    def __repr__(self):
        return 'Vect({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        if type(other) == type(self):
            return Vect(self.x + other.x, self.y + other.y)
        return Vect(self.x + other, self.y + other)

    def __iadd__(self, other):
        if type(other) == type(self):
            self.x += other.x
            self.y += other.y
            return self
        self.x += other
        self.y += other
        return self

    def __sub__(self, other):
        if type(other) == type(self):
            return Vect(self.x - other.x, self.y - other.y)
        return Vect(self.x - other, self.y - other)

    def __isub__(self, other):
        if type(other) == type(self):
            self.x -= other.x
            self.y -= other.y
            return self
        self.x -= other
        self.y -= other
        return self

    def __bool__(self):
        return self.x != 0 and self.y != 0

    def __neg__(self):
        return Vect(-self.x, -self.y)

    def __mul__(self, other):
        if type(other) == type(self):
            return self.x * other.x + self.y * other.y
        return Vect(self.x * other, self.y * other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def norm(self):
        hypot = abs(self)
        if hypot != 0:
            return Vect(self.x / hypot, self.y / hypot)
        return Vect(0, 0)

    def get_angel_cos(self, other):
        a = abs(self) * abs(other)
        b = (self * other) / a
        if b > 1:
            b = 1
        if b < -1:
            b = -1
        if a != 0:
            return b
        return 1

    def get_angel_r(self, other):
        return math.acos(self.get_angel_cos(other))

    def get_angel_g(self, other):
        return self.get_angel_r(other) * (180 / 3.1415)

    def rotate(self, a):
        x = self.x * math.cos(a) - self.y * math.sin(a)
        y = self.x * math.sin(a) + self.y * math.cos(a)
        return Vect(x, y)
