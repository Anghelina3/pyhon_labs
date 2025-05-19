from equation_solver import EquationSolver
from utils import input_vector, input_matrix

def main():
    solver = EquationSolver()
    while True:
        print("\n1. Работа с векторами")
        print("2. Работа с матрицами")
        print("3. Решение уравнений")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            from vector import Vector
            v1 = input_vector("Введите координаты первого вектора: ")
            v2 = input_vector("Введите координаты второго вектора: ")
            print("1. Длина первого вектора")
            print("2. Скалярное произведение")
            print("3. Угол между векторами")
            print("4. Сложение")
            print("5. Вычитание")
            print("6. Умножение на скаляр")
            print("7. Коллинеарность")
            op = input("Выберите операцию: ")
            try:
                if op == "1":
                    print("Длина:", v1.length())
                elif op == "2":
                    print("Скалярное произведение:", v1.dot_product(v2))
                elif op == "3":
                    print("Угол (в радианах):", v1.angle_with(v2))
                elif op == "4":
                    print("Сумма:", v1.add(v2))
                elif op == "5":
                    print("Разность:", v1.subtract(v2))
                elif op == "6":
                    scalar = float(input("Введите скаляр: "))
                    print("Результат:", v1.scalar_multiply(scalar))
                elif op == "7":
                    print("Коллинеарны:" if v1.is_collinear(v2) else "Не коллинеарны")
            except Exception as e:
                print("Ошибка:", e)

        elif choice == "2":
            from matrix import Matrix
            try:
                m1 = input_matrix()
                print("1. Сложение\n2. Вычитание\n3. Умножение на матрицу\n4. Умножение на вектор\n5. Транспонирование\n6. Определитель")
                op = input("Выберите операцию: ")
                if op in ["1", "2", "3"]:
                    m2 = input_matrix()
                    if op == "1":
                        print("Сумма:\n", m1.add(m2))
                    elif op == "2":
                        print("Разность:\n", m1.subtract(m2))
                    else:
                        print("Произведение:\n", m1.multiply_matrix(m2))
                elif op == "4":
                    v = input_vector("Введите вектор: ")
                    print("Результат:", m1.multiply_vector(v))
                elif op == "5":
                    print("Транспонированная матрица:\n", m1.transpose())
                elif op == "6":
                    print("Определитель:", m1.determinant())
            except Exception as e:
                print("Ошибка:", e)

        elif choice == "3":
            print("1. Линейное\n2. Квадратное\n3. Система линейных уравнений")
            op = input("Выберите тип уравнения: ")
            try:
                if op == "1":
                    a, b = map(float, input("Введите коэффициенты a и b: ").split())
                    print("Решение:", solver.solve_linear(a, b))
                elif op == "2":
                    a, b, c = map(float, input("Введите коэффициенты a, b, c: ").split())
                    print("Решения:", solver.solve_quadratic(a, b, c))
                elif op == "3":
                    m = input_matrix()
                    b = list(map(float, input("Введите правые части системы: ").split()))
                    print("Решения:", solver.solve_system(m, b))
            except Exception as e:
                print("Ошибка:", e)

        elif choice == "0":
            print("Завершение работы.")
            break
        else:
            print("Некорректный выбор. Повторите ввод.")

if __name__ == "__main__":
    main()
