from vector import Vector
from matrix import Matrix

def input_vector(prompt="Введите координаты вектора через пробел: "):
    coords = list(map(float, input(prompt).split()))
    return Vector(coords)

def input_matrix():
    r, c = map(int, input("Введите размер матрицы (строки и столбцы): ").split())
    rows = []
    print("Введите элементы матрицы:")
    for _ in range(r):
        row = list(map(float, input().split()))
        if len(row) != c:
            raise ValueError("Неверное количество элементов в строке")
        rows.append(row)
    return Matrix(rows)
