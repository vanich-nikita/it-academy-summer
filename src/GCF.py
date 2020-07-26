"""
Даны два натуральных числа.
Вычислите их наибольший общий делитель при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
"""


def gcf(a, b):
    if a >= 0 and b >= 0:
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a
    else:
        raise ValueError("Input positive number!")


if __name__ == '__main__':
    try:
        print(gcf(-10, -1))
    except ValueError:
        print("ValueError input correct data!")
    try:
        print(gcf('a', 'b'))
    except TypeError:
        print("TypeError input correct data!")
