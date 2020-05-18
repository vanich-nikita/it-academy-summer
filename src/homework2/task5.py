"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """
    # write your code here
    n1 = 0
    first = n1
    n2 = 1
    # Первые 2 числа Фибоначчи - могут быть 0,1 или 1,1
    for i in range(0, n - 2):
        fib = n1 + n2
        n1 = n2
        n2 = fib
    if n == 1:
        return first
    else:
        return n2  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = int(input("Enter your number: "))
    print(fibonacci(n))
