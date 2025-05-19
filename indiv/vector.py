import math

class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def length(self):
        return math.sqrt(sum(x ** 2 for x in self.coordinates))

    def dot_product(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Векторы должны быть одной размерности")
        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))

    def angle_with(self, other):
        dp = self.dot_product(other)
        len_self = self.length()
        len_other = other.length()
        return math.acos(dp / (len_self * len_other))

    def add(self, other):
        return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])

    def subtract(self, other):
        return Vector([a - b for a, b in zip(self.coordinates, other.coordinates)])

    def scalar_multiply(self, scalar):
        return Vector([scalar * x for x in self.coordinates])

    def is_collinear(self, other):
        ratio = None
        for a, b in zip(self.coordinates, other.coordinates):
            if b == 0:
                if a != 0:
                    return False
            else:
                if ratio is None:
                    ratio = a / b
                elif not math.isclose(a / b, ratio):
                    return False
        return True

    def __repr__(self):
        return f"Vector({self.coordinates})"
