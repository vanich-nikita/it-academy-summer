"""Определите, является ли число палиндромом (читается слева направо и справа
    налево одинаково).  Число положительное целое, произвольной длины. Задача
    требует работать только с числами (без конвертации числа в строку или
    что-нибудь еще)
"""


def palindrom(n):
    """Поиск числа фибоначчи.

    :param n: Число.
    :return: Bool. True или False. Является ли число палиндромом.
    """

    # write your code here
    rev = 0
    compare = n
    flag = False
    while n > 0:
        rev = (10 * rev) + n % 10
        n //= 10
    if compare == rev:
        flag =True
        print("The number entered is a palindrome")
    else:
        flag = False
        print("The entered number is NOT a palindrome")
    return flag  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = int(input("Enter your number: "))
    print(palindrom(n))
