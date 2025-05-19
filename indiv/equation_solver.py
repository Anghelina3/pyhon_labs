import math

class EquationSolver:
    def solve_linear(self, a, b):
        if a == 0:
            return "Нет решения" if b != 0 else "Бесконечно много решений"
        return -b / a

    def solve_quadratic(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d < 0:
            return "Нет вещественных корней"
        elif d == 0:
            return [-b / (2 * a)]
        else:
            sqrt_d = math.sqrt(d)
            return [(-b + sqrt_d) / (2 * a), (-b - sqrt_d) / (2 * a)]

    def solve_system(self, matrix, b):
        return matrix.solve_gauss(b)
