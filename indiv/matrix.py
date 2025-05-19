from copy import deepcopy

class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def add(self, other):
        return Matrix([[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(self.rows, other.rows)])

    def subtract(self, other):
        return Matrix([[a - b for a, b in zip(r1, r2)] for r1, r2 in zip(self.rows, other.rows)])

    def multiply_matrix(self, other):
        result = []
        for row in self.rows:
            result_row = []
            for col in zip(*other.rows):
                result_row.append(sum(a * b for a, b in zip(row, col)))
            result.append(result_row)
        return Matrix(result)

    def multiply_vector(self, vector):
        return [sum(a * b for a, b in zip(row, vector.coordinates)) for row in self.rows]

    def transpose(self):
        return Matrix([list(col) for col in zip(*self.rows)])

    def determinant(self):
        if len(self.rows) != len(self.rows[0]):
            raise ValueError("Матрица должна быть квадратной")
        return self._determinant_recursive(self.rows)

    def _determinant_recursive(self, matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = 0
        for c in range(len(matrix)):
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            det += ((-1) ** c) * matrix[0][c] * self._determinant_recursive(minor)
        return det

    def solve_gauss(self, b):
        a = deepcopy(self.rows)
        n = len(a)
        for i in range(n):
            max_row = max(range(i, n), key=lambda r: abs(a[r][i]))
            a[i], a[max_row] = a[max_row], a[i]
            b[i], b[max_row] = b[max_row], b[i]
            for j in range(i + 1, n):
                factor = a[j][i] / a[i][i]
                for k in range(i, n):
                    a[j][k] -= factor * a[i][k]
                b[j] -= factor * b[i]
        x = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(i + 1, n))) / a[i][i]
        return x

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.rows])
